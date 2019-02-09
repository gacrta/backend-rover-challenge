class Rover:
	""" The exploration rover class. """

	#		N
	#	W 	+	E
	#		S

	def __init__(self, rover_position):
		"""(Rover, (int, int, str) tuple)) -> NoneType

		Inits Rover object and stores its initial position

		>>> rover = Rover((10, 30, "N"))
		>>> rover.x
		10
		>>> rover.y
		30
		>>> rover.direction
		'N'
		"""
		self.x = rover_position[0]
		self.y = rover_position[1]
		self.direction = rover_position[2]

	def move_foward(self):
		"""(Rover) -> NoneType

		Moves the rover in the direction it is facing.
		>>> pos = (1, 1, 'N')
		>>> r = rover.Rover(pos)
		>>> r.move_foward()
		>>> (r.x, r.y)
		(1, 2)
		>>> pos = (3, 1, 'W')
		>>> r = rover.Rover(pos)
		>>> r.move_foward()
		>>> (r.x, r.y)
		(2, 1)
		"""

		if self.direction == "N":
			self.y += 1

		elif self.direction == "E":
			self.x += 1

		elif self.direction == 'S':
			self.y -= 1

		else:
			self.x -= 1


	def turn_left(self):
		"""(Rover) -> NoneType

		Turns the rover in the left direction.
		>>> pos = (1, 1, 'N')
		>>> r = rover.Rover(pos)
		>>> r.turn_left()
		>>> (r.x, r.y, r.direction)
		(1, 2, 'W')
		>>> pos = (3, 1, 'E')
		>>> r = rover.Rover(pos)
		>>> r.turn_left()
		>>> (r.x, r.y, r.direction)
		(3, 1, 'N')
		"""

		if self.direction == "N":
			self.direction = 'W'

		elif self.direction == "W":
			self.direction = 'S'

		elif self.direction == 'S':
			self.direction = 'E'

		else:
			self.direction = 'N'

	def turn_right(self):
		"""(Rover) -> NoneType

		Turns the rover in the right direction.
		>>> pos = (1, 1, 'N')
		>>> r = rover.Rover(pos)
		>>> r.turn_right()
		>>> (r.x, r.y, r.direction)
		(1, 2, 'E')
		>>> pos = (3, 1, 'E')
		>>> r = rover.Rover(pos)
		>>> r.turn_right()
		>>> (r.x, r.y, r.direction)
		(3, 1, 'S')
		"""
		
		if self.direction == "N":
			self.direction = 'E'

		elif self.direction == "E":
			self.direction = 'S'

		elif self.direction == 'S':
			self.direction = 'W'

		else:
			self.direction = 'N'

	def get_position(self):
		"""(Rover) -> (int, int, str) tuple

		Return the current rover position tuple.

		>>> pos = (1, 2, 'N')
		>>> r = rover.Rover(pos)
		>>> r.get_position()
		(1, 2, 'N')

		"""
		pos = (self.x, self.y, self.direction)
		return pos