import mysql.connector

con = mysql.connector.connect(user='localhost',password='',host='127.0.0.1',database='blg')

cursor = con.cursor()
cursor.execute('select * from posts')
data = cursor.fetchone()
print('data'+data)
con.close()
'''
'''
