#from AddCommand import AddCommand
#from ListCommand import ListCommand
#from HelpCommand import HelpCommand

class CommandFactory(object):

	def get_command(command_string):
		def command_map(string):
			return {
				'add' : AddCommand(),
				'list' : ListCommand()
			}.get(string, HelpCommand())

		return command_map(command_string)