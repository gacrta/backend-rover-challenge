from rover_project import reader
import unittest

class TestReaderReadUpperRightCoord(unittest.TestCase):
	""" Test Class for Reader.has_rover_simulation
		method at reader module.
	"""
	file_path = 'rover_project/tests/'

	def test_has_rover_simulation_found(self):
		"""
		Test if reader correctly peeks next line of
		input file to check if there is still content
		and succeeds.
		"""

		filename = TestReaderReadUpperRightCoord.file_path + "test_reader_coords.txt"

		with reader.Reader(filename) as r:
			# read a couple of lines
			_ = r.readline()
			_ = r.readline()

			self.assertTrue(has_rover_simulation())

	def test_has_rover_simulation_not_found(self):
		"""
		Test if reader correctly peeks next line of
		input file to check if there is still content
		and fails.
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