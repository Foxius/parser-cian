import sqlite3
from contextlib import closing
import contextlib

path_db = 'db.sqlite3'



def add_user(user_id):
	with contextlib.closing(sqlite3.connect(path_db)) as conn:
		with conn:
			with contextlib.closing(conn.cursor()) as cursor:
				r = cursor.execute('SELECT * FROM users WHERE user_id = ?;', [user_id]).fetchone()
				if r is None:
					cursor.execute('INSERT INTO users (user_id) VALUES (?);', [user_id])



def add_url(user_id, url, amount):
	with contextlib.closing(sqlite3.connect(path_db)) as conn:
		with conn:
			with contextlib.closing(conn.cursor()) as cursor:
				r = cursor.execute('SELECT * FROM urls WHERE url = ? AND user_id = ?;', (url, user_id)).fetchone()
				if r is None:
					cursor.execute('INSERT INTO urls (url, user_id, last_amount, sub) VALUES (?, ?, ?, ?);', (url, user_id, amount, 1))



def update_sub(user_id, url, sub):
	with contextlib.closing(sqlite3.connect(path_db)) as conn:
		with conn: 
			with contextlib.closing(conn.cursor()) as cursor: 
				users = cursor.execute('UPDATE urls SET sub = ? WHERE user_id = ?;', (sub, user_id))




def select_by_url(url):
	with contextlib.closing(sqlite3.connect(path_db)) as conn:
		with conn: 
			with contextlib.closing(conn.cursor()) as cursor: 
				users = cursor.execute('SELECT * FROM urls WHERE url = ? AND sub = 1;', [url]).fetchall()
				return users


def get_all():
	with contextlib.closing(sqlite3.connect(path_db)) as conn:
		with conn: 
			with contextlib.closing(conn.cursor()) as cursor: 
				alls = cursor.execute('SELECT * FROM urls WHERE sub = 1;').fetchall()
				return alls