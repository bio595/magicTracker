import sqlite3

instance = None

def get_DBHelper_instance():

	class DBHelper(object):
		
		def __init__(self):
			#open the connections
			conn = sqlite3.connect('magic.db')

			#create the tables if they dont exist
			cursor = conn.cursor()
			cursor.execute("""CREATE TABLE IF NOT EXISTS decks
							(
								name TEXT,
								version INTEGER,
								color TEXT,
								creator TEXT
							 PRIMARY KEY (name, version));""")

			cursor.execute(""" CREATE TABLE IF NOT EXISTS games
				(
					dateTime DATETIME PRIMARY KEY,
					winningPlayer TEXT,
					winningDeckName TEXT,
					winningDeckVersion INTEGER,
					winningMulligans INTEGER,
					losingPlayer TEXT,
					losingDeckName TEXT,
					losingDeckVesrion INTEGER,
					losingMulligans INTEGER
					
				);""")
			conn.commit()
			conn.close()
		
		def addDeck(self, name, version, color, creator):
			#open the connections
			with sqlite3.connect('magic.db') as conn:
				cursor = conn.cursor()
				cursor.execute("""INSERT INTO decks (
								name, version, color, creator, wins, losses
								)
								VALUES (
								?, ?, ?, ?, 0, 0
								);""", (name, version, color, creator))

				conn.commit()

	global instance
	if instance is None:
		instance = DBHelper()
	return instance