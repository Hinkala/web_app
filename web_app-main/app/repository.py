import sqlite3


db_name = "cats_db"


def check_credentials(login, password):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials where login=? and password=?;", (login, password))
	user = cursor.fetchall()
	print(user)
	return user[0]

def check_login(login):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials where login=?;",(login,))
	if cursor.fetchall():
		return False
	else:
		return True

def create_credentials(credentials):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO user(name),values (NULL);")
	cursor.execute("INSERT INTO credentials(login,password) values (?,?,?)",(credentials.login,credentials.password,credentials.user_id))
	connection.commit()