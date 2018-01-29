import sqlite3

conn = sqlite3.connect("test.db")
conn.execute("create table if not exists address(id integer primary key autoincrement, name varchar(128), address varchar(128))")

conn.execute("insert into address(name, address) values('Lions', 'Suzhou')")

conn.commit()

cursor = conn.cursor()
cursor.execute("select * from address")

result = cursor.fetchall()

for record in result:
	for feild in record:
		print feild,
	print

cursor.close()
conn.close()

