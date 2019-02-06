from rover_project import reader
import unittest

class TestReaderReadUpperRightCoord(unittest.TestCase):
	""" Test Class for Reader.read_upper_right_coordinates
		method at reader module.
	"""
	file_path = 'rover_project/tests/'

	def test_reader_read_x_coord(self):
		"""
		Test if reader gets correct x_coord from
		a file that contains 4 5 information.
		"""

		filename = TestReaderReadUpperRightCoord.file_path + "test_reader_coords.txt"

		with reader.Reader(filename) as r:
			x_coord, y_coord = r.read_upper_right_coordinates()

		self.assertEqual(x_coord, 4)

	def test_reader_read_y_coord(self):
		"""
		Test if reader gets correct y_coord from
		a file that contains 4 5 information.
		"""

		filename = TestReaderReadUpperRightCoord.file_path + "test_reader_coords.txt"

		with reader.Reader(filename) as r:
			x_coord, y_coord = r.read_upper_right_coordinates()

		self.assertEqual(y_coord, 5)

	def test_reader_wrong_input(self):
		"""
		Test if reader avoids wrong input and don't
		crash.
		"""

		filename = TestReaderReadUpperRightCoord.file_path + "test_reader_wrong_input.txt"

		with reader.Reader(filename) as r:
			self.assertRaises(ValueError, r.read_upper_right_coordinates)

if __name__ == "__main__":
	unittest.main(exit=False)