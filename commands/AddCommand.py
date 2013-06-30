from dbhelper import get_DBHelper_instance

class AddCommand(object):
	
	def __init__(self, argv):
		self.argv = argv

	def execute(self):
		if not len(self.argv) > 1:
			print "Not enough arguments supplied"
		else:
			if self.argv[1] == 'deck':
				if not len(self.argv) == 6:
					print "Wrong number of arguments supplied"
				else:
					get_DBHelper_instance().addDeck(self.argv[2], #name
													self.argv[3], #version
													self.argv[4], #colour
													self.argv[5]) #creator
			
			elif self.argv[1] == 'result':
				if not len(self.argv) == 10:
					print "Wrong number of arguments supplied"
				else:
					get_DBHelper_instance().addResult(self.argv[2], #winner name 
													  self.argv[3], #winner deck
													  self.argv[4], #winner version
													  self.argv[5], #winner mulligans
													  self.argv[6], #loser name
													  self.argv[7], #loser deck
													  self.argv[8], #loser version
													  self.argv[9]) #loser mulligans
			

