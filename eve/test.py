from sqlite import Sqlite




sqlite = Sqlite()

sqlite.open("test.db")

sqlite.execute("create table if not exists projects(id integer primary key autoincrement, project_name varchar(128))")
result = sqlite.execute("select * from projects")
for record in result:
	for field in record:
		print field

name = "test"
sqlite.execute("insert into projects(project_name) values('%s')"%(name))

sqlite.close()






