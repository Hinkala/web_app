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