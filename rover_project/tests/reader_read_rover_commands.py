from rover_project import reader
import unittest

class TestReaderReadRoverCommands(unittest.TestCase):
	""" Test Class for Reader.read_rover_commands
		method at reader module.
	"""
	file_path = 'rover_project/tests/'

	def test_reader_read_empty_line(self):
		"""
		Test if reader gets empty list if
		line has zero commands.
		"""

		filename = TestReaderReadRoverCommands.file_path + "test_reader_zero_input.txt"

		with reader.Reader(filename) as r:
			commands = r.read_rover_commands()

		self.assertEqual(commands, [])

	def test_reader_read_one_input(self):
		"""
		Test if reader get correct command from file
		with only one command: A.
		"""

		filename = TestReaderReadRoverCommands.file_path + "test_reader_one_input.txt"

		with reader.Reader(filename) as r:
			commands = r.read_rover_commands()

		self.assertEqual(commands, ['A'])

	def test_reader_read_command_line(self):
		"""
		Test if reader gets correct command list
		from a file that contains ABCDEF information.
		"""

		filename = TestReaderReadRoverCommands.file_path + "test_reader_commands.txt"

		with reader.Reader(filename) as r:
			commands = r.read_rover_commands()

		self.assertEqual(commands, ['A','B', 'C', 'D', 'E', 'F'])

if __name__ == "__main__":
	unittest.main(exit=False)