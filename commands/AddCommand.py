from dbhelper import DBHelper

class AddCommand(object):
	
	def __init__(self, argv):
		self.argv = argv

	def execute(self):
		DBHelper().addDeck(self.argv[1], self.argv[2], self.argv[3], self.argv[4])


		