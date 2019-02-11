from rover_project import reader
import unittest

class TestReaderReadRoverStartingPosition(unittest.TestCase):
	""" Test Class for Reader.read_rover_starting_position
		method at reader module.
	"""
	file_path = 'rover_project/tests/'

	def test_reader_read_x_coord(self):
		"""
		Test if reader gets correct x_coord from
		a file that contains 3 1 N information.
		"""

		filename = TestReaderReadRoverStartingPosition.file_path + "test_reader_rover_pos.txt"

		with reader.Reader(filename) as r:
			x_coord, y_coord, direction = r.read_rover_starting_position()

		self.assertEqual(x_coord, 3)

	def test_reader_read_y_coord(self):
		"""
		Test if reader gets correct y_coord from
		a file that contains 3 1 N information.
		"""

		filename = TestReaderReadRoverStartingPosition.file_path + "test_reader_rover_pos.txt"

		with reader.Reader(filename) as r:
			x_coord, y_coord, direction = r.read_rover_starting_position()

		self.assertEqual(y_coord, 1)

	def test_reader_read_direction(self):
		"""
		Test if reader gets correct direction from
		a file that contains 3 1 N information.
		"""

		filename = TestReaderReadRoverStartingPosition.file_path + "test_reader_rover_pos.txt"

		with reader.Reader(filename) as r:
			x_coord, y_coord, direction = r.read_rover_starting_position()
		self.assertEqual(direction, 'N')

	def test_reader_wrong_input(self):
		"""
		Test if reader avoids wrong input and don't
		crash.
		"""

		filename = TestReaderReadRoverStartingPosition.file_path + "test_reader_wrong_input.txt"

		with reader.Reader(filename) as r:
			self.assertRaises(ValueError, r.read_upper_right_coordinates)

if __name__ == "__main__":
	unittest.main(exit=False)