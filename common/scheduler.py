import psycopg2
import sys

'''
   Algorithm to create a schedule for a ten week season 
'''


def scheduler(**kwargs):
    print ('Connecting to database')
    conn = psycopg2.connect("dbname={0} user={1}".format(kwargs['db_name'], kwargs['user']))
    c = conn.cursor()

    # get the users in the selected league
    c.execute('select au.id from auth_user au inner join home_profile hp on au.id = hp.user_id where hp.league_id = 2')
    users = c.fetchall()

    # list that contains the schedule
    schedule = []

    # if the team has an odd amount of people add a bye team to the results
    if len(users) % 2 != 0:
        users.append((-1, ))

    # create rows for a matchup against a different team each week
    print ('Generating and inserting rows')
    for i in range(len(users)-1):
        mid = len(users) / 2
        l1 = users[:mid]
        l2 = users[mid:]
        l2.reverse()

        # Switch sides after each round
        if i % 2 == 1:
            schedule = [zip(l1, l2)]
        else:
            schedule = [zip(l2, l1)]

        users.insert(1, users.pop())

        # insert matchups for each pair into the database
        for list_of_matchups in schedule:
            for matchup in list_of_matchups:
                c.execute('insert into home_schedule (user_id, opponent, week) values (%s, %s, %s)', (matchup[0][0], matchup[1][0], i + 1))
                c.execute('insert into home_schedule (user_id, opponent, week) values (%s, %s, %s)', (matchup[1][0], matchup[0][0], i + 1))

    print ('Committing changes to the database')
    conn.commit()
    print ('Closing connections')
    c.close()
    conn.close()


def main():
    db_name = sys.argv[1]
    user = sys.argv[2]
    league_id = sys.argv[3]
    try:
        scheduler(db_name=db_name, user=user, league_id=league_id)
    except IndexError:
        print ('Command incorrect')
        print ('Correct input is: python scheduler.py db_name user league_id')

main()
