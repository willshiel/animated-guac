import psycopg2
import sys
'''
    A python script to delete users that have no associated profile.
    This script will be run once a day to ensure database integrity.
'''

def user_deletion(**kwargs):
    print ('Connecting to database')
    conn = psycopg2.connect("dbname={0} user={1}".format(kwargs['db_name'], kwargs['db_user']))
    c = conn.cursor()

    # get the users that don't have a profile
    c.execute('''select id from auth_user where id not in 
                 (
                    select au.id from auth_user au
                    inner join home_profile hp
                    on au.id = hp.user_id
                 )
              ''')

    # delete each user
    unbound_users = c.fetchall()
    for user in unbound_users:
        c.execute('delete from auth_user where id = %s', [user[0]])

    # commit changes and close all references to the db
    conn.commit()
    c.close()
    conn.close()


def main():
    db_name = sys.argv[1]
    db_user = sys.argv[2]
    try:
        user_deletion(db_name=db_name, db_user=db_user)
    except IndexError:
        print ('Command incorrect')
        print ('Correct input is: python unbound_user_deletion.py db_name db_user')

main()
