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
					#name, version, colour, creator
					get_DBHelper_instance().addDeck(self.argv[2], self.argv[3], self.argv[4], self.argv[5])
			elif self.argv[1] == 'result':
				pass
			

