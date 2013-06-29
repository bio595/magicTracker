from AddCommand import AddCommand
from ListCommand import ListCommand
from HelpCommand import HelpCommand
from ResultCommand import ResultCommand

def get_command(command_string):
	def command_map(arguments):
		return {
			'add' : AddCommand(arguments),
			'list' : ListCommand(arguments),
			'wins' : ResultCommand(arguments)
		}.get(arguments[0], HelpCommand(arguments[1:]))

	return command_map(command_string)