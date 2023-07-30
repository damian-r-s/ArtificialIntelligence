from dbmodule import connect

connection = connect('db name', 'username', 'pswd')

cursor = connection.cursor()

cursor.execute('select * from mytable')
results = cursor.fetchall()

cursor.close()
connection.close()