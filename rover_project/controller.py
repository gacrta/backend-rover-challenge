from rover_project import reader
from rover_project import rover

class Controller:
	""" The Rover Controller class. """

	#		N
	#	W 	+	E
	#		S

	def __init__(self, filename):
		"""(Controller, str) -> NoneType

		Inits Controller object. It receives the input
		filename and try to access it with a reader object
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> Controller("input.txt")
		...
		>>> Controller("no_such_file.txt")
		FileNotFound
		"""
		self.reader = reader.Reader(filename)

	def init_plateau(self):
		"""(Controller) -> NoneType

		Reads the plateau right-upper coordinates 
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.init_plateau()
		>>> c.x_limit
		5
		>>> c.y_limit
		5
		"""
		return None

	def init_rover(self):
		"""(Controller) -> NoneType

		Init the rover at position defined by input file.
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.init_rover()
		>>> c.rover.x
		1
		>>> c.rover.y
		2
		>>> c.rover.direction
		"N"
		"""

		return None

	def run_commands(self):
		"""(Controller) -> NoneType

		Get and run the rover commands as defined by
		input file.
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.init_rover()
		>>> c.run_commands()
		>>> c.rover.x
		1
		>>> c.rover.y
		3
		>>> c.rover.direction
		"N"
		"""

		return None

	def get_rover_position(self):
		"""(Controller) -> (int, int, str) tuple

		Return the rover position tuple.

		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.init_rover()
		>>> c.run_commands()
		>>> c.get_rover_position()
		(1,	3, "N")
		"""

		return None