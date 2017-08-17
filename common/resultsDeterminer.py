import psycopg2
import sys
from current_week import CURRENT_WEEK

'''
    Python script to determine the results for all of the picks made
    and neatly put them into the database
'''

def results(**kwargs):
    print ('Connecting to database')
    conn = psycopg2.connect("dbname={0} user={1}".format(kwargs['db_name'], kwargs['db_user']))
    c = conn.cursor()

    # get the users in the league, place them in a list of tuples
    c.execute('select user_id from home_profile where league_id = {0}'.format(kwargs['league_id']))
    users = c.fetchall()

    # loop through each user to calculate their results
    for user in users:

        total_points = 0

        # get the picks the user has made
        sql = 'select team_picked_id, margin from picks_pick pp where user_id = {0}'.format(user[0])
        c.execute(sql)
        picks = c.fetchall()

        # compare the pick to the the actual result
        for pick in picks:

            points = 0

            sql = 'select winning_team_id, margin, underdog from picks_game where home_team_id = {0} or away_team_id = {0}'.format(pick[0])
            c.execute(sql)
            game = c.fetchone()

            # if the game was a tie
            if game is None:
                continue

            # if the selection made was correct
            if pick[0] == game[0]:
                points += 3

                # if the team is also the underdog
                if game[0] == game[2]:
                    points += 1

                # if the margin was within one or correct
                if pick[1] == (game[1] - 1) or pick[1] == (game[1] + 1) or pick[1] == game[1]:
                    points += 1

                    if pick[1] == game[1]:
                        points += 1

            total_points += points
            print ('Pick: {0}, Game: {1}, TotalPoints: {2}'.format(pick[0], game[0], total_points))

        print ('{0}: {1}'.format(user[0], total_points))

        # insert their total points into the db
        print ('Beginning insert')
        #c.execute('insert into home_pointsforweek (week, points, user_id) values (%s, %s, %s)', (CURRENT_WEEK, total_points, user[0]))
        print ('Insert finished')

    print ('Comparing scores now')
    count = 0
    for user in users:

        # get the user's opponent
        c.execute('select opponent from home_schedule where week = %s and user_id = %s', (CURRENT_WEEK, user[0]))
        opponent = c.fetchone()

        # if the user has a bye
        if (opponent[0] == -1 or user[0] == -1):
            continue

        # get the amount of points each team scored
        c.execute('select points from home_pointsforweek where (user_id = %s or user_id = %s) and week = %s', (user[0], opponent[0], CURRENT_WEEK))
        points = c.fetchall()

        print ('User: {0}-{1} Opponent: {2}-{3}'.format(user[0], points[0], opponent[0], points[1]))

        # compare points
        if points[0] > points[1]:
            c.execute('update home_record set wins = wins + 1 where user_id = %s', [user[0]])
            c.execute('update home_record set losses = losses + 1 where user_id = %s', [opponent[0]])
        elif points[1] > points[0]:
            c.execute('update home_record set wins = wins + 1 where user_id = %s', [opponent[0]])
            c.execute('update home_record set losses = losses + 1 where user_id = %s', [user[0]])
        else:
            c.execute('update home_record set ties = ties + 1 where user_id = %s or user_id = %s', [user[0], opponent[0]])

        # remove the already updated opponent from the list
        for item in users:
            if opponent[0] == item[0]:
                users.remove(item)

    #conn.commit()
    c.close()
    conn.close()



def main():
    db_name = sys.argv[1]
    db_user = sys.argv[2]
    league_id = sys.argv[3]
    results(db_name=db_name, db_user=db_user, league_id=league_id)

main()



