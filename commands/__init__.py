from AddCommand import AddCommand
from ListCommand import ListCommand
from HelpCommand import HelpCommand



def get_command(command_string):
	def command_map(arguments):
		return {
			'add' : AddCommand(arguments),
			'list' : ListCommand(arguments)
		}.get(arguments[0], HelpCommand(arguments))

	return command_map(command_string)