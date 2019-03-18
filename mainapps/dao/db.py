# coding:utf-8

import pymysql

config = {
   'host': '127.0.0.1',
   'port': 3306,
   'user': 'root',
   'password': 'root',
   'db': 'stu',
   'charset': 'utf8'
}

print('-- Connection DB model----')

class DB():
   def __init__(self):
       self.connection()

   def connection(self):
       self.conn = pymysql.Connect(**config)
       print('--Connected OK--')

   def __enter__(self):
       return self.conn.cursor()


   def __exit__(self, exce_type, values, traceback):
       if exce_type:
          self.conn.rollback
       else:
          self.conn.commit()

       self.conn.close()
