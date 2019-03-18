from django.test import TestCase
from django.db import connection


# Create your tests here.
class TestSQLQuery(TestCase):
    def test_query1(self):
        cursor = connection.cursor()
        cursor.execute('select * from t_tage')
        for row in cursor.fetchall():
            print(row)
