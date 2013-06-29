import sqlite3

class DBHelper(object):
	
	def __init__(self):
		#open the connections
		self.conn = sqlite3.connect('magic.db')

		#create the tables if they dont exist
		cursor = self.conn.cursor()
		cursor.execute("""CREATE TABLE IF NOT EXISTS decks
						(
							name TEXT,
							version INTEGER,
							color TEXT,
							creator TEXT,
							wins INTEGER,
							losses INTEGER,
						 PRIMARY KEY (name, version));""")

	def __del__(self):
		self.conn.close()
		