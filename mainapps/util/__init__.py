from django.db import connection


def query1():
    cursor = connection.cursor()
    cursor.execute('select * from t_tag')
    for row in cursor.fetchall():
        print(row)
