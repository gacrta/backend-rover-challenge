class Reader:
	""" The rover input file reader. """

	def __init__(self, filename):
		"""(Reader, str) -> NoneType

		Inits Reader object with a with a filename

		>>> file1 = 'filename.txt'
		>>> reader = Reader(file1)
		>>> reader.filename == 'filename.txt'
		True
		>>> reader.file == None
		True
		"""
		self.filename = ''
		self.file = None

	def open():
		"""(Reader) -> NoneType

		Opens the file with name self.filename for reading.
		and stores it at self.file. self.file must be closed
		after used.

		>>> reader = Reader('')
		>>> reader.file == None
		False
		"""
		return None

	def close():
		"""(Reader) -> NoneType

		Closes the file at self.file that was opened by
		self.open(). After closed, in order to read from
		the file again it is necessary to re-open the file.

		>>> reader = Reader('')
		>>> reader.close()
		>>> reader.file == None
		False
		>>> reader.file.readline()
		Traceback (most recent call last):
			File "<stdin>", line 1, in <module>
		ValueError: I/O operation on closed file.
		"""
		return None

	def read_upper_right_coordinates(self):
		"""(Reader) -> (int, int) tuple

		Reads the first line at file refered as
		this.filename and returns a tuple of
		(plateau_vertical, plateau_horizontal)

		>>> echo 4 4 >> test.txt
		>>> r = Reader('test.txt')
		>>> size_x, size_y = r.read_upper_right_coordinates()
		>>> size_x == 4
		True
		>>> size_y == 4
		True
		"""
		return (0, 0)

	def read_rover_starting_position(self):
		"""(Reader) -> (int, int, str) tuple

		Reads a line with rover starting position
		and return a tuple with
		(rover_x, rover_y, orientation) information.

		>>> echo 1 2 E >> test.txt
		>>> r = Reader('test.txt')
		>>> rover_x, rover_y, orientation = r.read_rover_starting_position()
		>>> rover_x == 1
		True
		>>> rover_y == 2
		True
		>>> orientation == 'E'
		True
		"""
		return (0, 0, 'E')

	def read_rover_commands(self):
		"""(Reader) -> List of str

		Reads a line with commands separated by space
		and return a list of individual string commands.

		>>> echo M R M L L M >> test.txt
		>>> r = Reader('test.txt')
		>>> commands = r.read_rover_commands()
		>>> commands == ['M', 'R', 'M', 'L', 'L', 'M']
		True
		"""
		return []