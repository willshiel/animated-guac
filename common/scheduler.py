import psycopg2

'''
    This is a script for generating a schedule for a certain league
    it is taken from an algorithm called round robin
    corresponding stack overflow:
        https://stackoverflow.com/questions/1037057/how-to-automatically-generate-a-sports-league-schedule
'''

def scheduler():
    print 'Connecting to database'
    conn = psycopg2.connect("dbname=gettingstarted user=will")
    c = conn.cursor()
    c.execute('select id from auth_user')
    users_tuple = c.fetchall()
    matchups_by_week = []
    users = [i[0] for i in users_tuple]

    # create schedule
    if len(users) % 2 == 1:
        users = users + '-1'
    for i in range(0, len(users)-1):
        mid = len(users) / 2
        l1 = users[:mid]
        l2 = users[mid:]

        # switch sides after each round
        if i % 2 == 1:
            matchups_by_week = matchups_by_week + [zip(l1, l2)]
        else:
            matchups_by_week = matchups_by_week + [zip(l2, l1)]

        users.insert(1, users.pop())

    # add each matchup to each database, count tracks the week
    print 'beginning the entries'
    count = 1
    for week in matchups_by_week:
        print 'You got to week'
        for matchup in week:
            print 'You got to inserts'
            sql = "insert into home_schedule (user_id, opponent, week) values (%s, %s, %s)"
            data = (matchup[0], matchup[1], count)
            c.execute(sql, data)
            'You have executed one'
            data = (matchup[1], matchup[0], count)
            c.execute(sql, data)
        count += 1

    print 'Your data has been entered'

    conn.commit()
    c.close()
    conn.close()

def main():
    scheduler()

main()