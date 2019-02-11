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
		#self.reader = reader.Reader(filename)
		self.filename = filename
		self.x_limit = 0
		self.y_limit = 0

	def run(self):
		"""(Controller) -> NoneType

		Executes all lines of input file.
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.run()
		1 3 N
		"""

		with Reader.reader(self.filename) as r:
			self.x_limit, self.y_limit = r.read_upper_right_coordinates()
			while r.has_rover_simulation():
				rover_starting_position = r.read_rover_starting_position()
				m_rover = rover.Rover(rover_starting_position)
				commands = r.read_rover_commands()
				for command in commands:
					do_command(m_rover, command)
				print( format_position( m_rover.get_position() ) )

	def do_command(self, a_rover, command):
		"""(Controller, rover, str) -> NoneType

		Get the rover do a specific commands represented
		as a character as 'M', 'R' and 'L'
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.init_rover()
		>>> c.do_command('M')
		>>> c.rover.x
		1
		>>> c.rover.y
		3
		>>> c.rover.direction
		"N"
		>>> c.do_command('R')
		>>> c.rover.x
		1
		>>> c.rover.y
		3
		>>> c.rover.direction
		"E"
		>>> c.do_command('L')
		>>> c.rover.x
		1
		>>> c.rover.y
		3
		>>> c.rover.direction
		"N"
		"""

		rover_x, rover_y, rover_direction = a_rover.get_position()
		if command == 'M':
			if rover_direction == 'N' and rover_y < self.y_limit:
				a_rover.move_foward()
			elif rover_direction == 'E' and rover_x < self.x_limit:
				a_rover.move_foward()
			elif rover_direction == 'S' and rover_y > 0:
				a_rover.move_foward()
			elif rover_direction == 'W' and rover_x > 0:
				a_rover.move_foward()

		elif command == 'L':
			a_rover.turn_left()

		elif command == 'R':
			a_rover.turn_right()

	def format_position(self, rover_position):
		"""(Controller, (int, int, str) tuple) -> str

		Formats a string with rover position 
		>>> cat input.txt
		5 5
		1 2 N
		LMLMLMLMM
		>>> c = Controller("input.txt")
		>>> c.run()
		1 3 N
		>>> c.format_position()
		1 3 N
		"""

		return ""