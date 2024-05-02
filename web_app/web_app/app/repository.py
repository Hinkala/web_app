import sqlite3
from app import model

db_name = "cats_db"


def check_credentials(login, password):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials where login=? and password=?;", (login, password))
	user = cursor.fetchone()
	if user:
		print(user)
		return model.Credentials(user[0], user[1], user[2], user[3])
	else:
		return None


def check_login(login):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials where login=?;",(login,))
	if cursor.fetchone():
		return False
	else:
		return True


def create_credentials(credentials):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("INSERT INTO user(name) values (NULL);")
	user_id = cursor.lastrowid
	cursor.execute("INSERT INTO credentials(login,password, user_id) values (?,?,?)", (credentials.login, credentials.password, user_id))
	connection.commit()


def get_credentials_by_id(user_id):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM user where id=?;", (user_id,))
	one = cursor.fetchone()
	if one:
		credentials = model.User(one[0], one[1], one[2], one[3])
		return credentials
	else:
		return None


def authorize_user(login, password):
	connection = sqlite3.connect(db_name)
	connection.set_trace_callback(print)
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM credentials WHERE  login = ?;", (login,))
	row = cursor.fetchone()
	if row:
		if row[2] == password:
			cursor.execute("SELECT * FROM user WHERE id = ?;", (row[0],))
			user = cursor.fetchone()
			if user:
				auth_user = model.User(user[0], user[1], user[2], user[3])
				return auth_user
			else:
				return None
	return None
