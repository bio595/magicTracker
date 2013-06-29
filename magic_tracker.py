from sys import argv
from commands import get_command

def main():

	if len(argv) == 1:
		from dbhelper import DBHelper
		var = DBHelper()
		with open('description.txt') as f:
			print f.read()
	else:
		command = argv[1]
		command = get_command(argv[1:])
		command.execute()


if __name__ == '__main__':
	main()