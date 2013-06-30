import sqlite3

instance = None

def get_DBHelper_instance():

	class DBHelper(object):

		def __init__(self):

			self.db_path = 'magic.db?PRAGMA foreign_keys = ON;'
			#open the connections
			with sqlite3.connect(self.db_path) as conn:

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
						dateTime DATETIME DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
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
		
		def addDeck(self, name, version, color, creator):
			#open the connections
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute("""INSERT INTO decks (
								name, version, color, creator, wins, losses
								)
								VALUES (
								?, ?, ?, ?, 0, 0
								);""", (name, version, color, creator))

				conn.commit()
		def addResult(self, winner_name, winner_deck, winner_version, winner_mulligans, loser_name, loser_deck, loser_version, loser_mulligans):
			with sqlite3.connect(self.db_path) as conn:
				cursor = conn.cursor()
				cursor.execute("""INSERT INTO games (
								winningPlayer,
								winningDeckName,
								winningDeckVersion,
								winningMulligans,
								losingPlayer,
								losingDeckName,
								losingDeckVesrion,
								losingMulligans 
								) VALUES (
								?, ?, ?, ?, ?, ?, ?, ?)""", (winner_name, winner_deck, winner_version, winner_mulligans, loser_name, loser_deck, loser_version, loser_mulligans))
				conn.commit()

	global instance
	if instance is None:
		instance = DBHelper()
	return instance