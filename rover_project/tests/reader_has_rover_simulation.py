from rover_project import reader
import unittest

class TestReaderHasRoverSim(unittest.TestCase):
	""" Test Class for Reader.read_upper_right_coordinates
		method at reader module.
	"""
	file_path = 'rover_project/tests/'

	def test_has_rover_simulation_found(self):
		"""
		Test if reader correctly peeks next line of
		input file to check if there is still content
		and succeeds.
		"""

		filename = TestReaderHasRoverSim.file_path + "test_3_line_file.txt"

		with reader.Reader(filename) as r:
			# read a couple of lines
			_ = r.file.readline()
			_ = r.file.readline()

			self.assertTrue(r.has_rover_simulation())

	def test_has_rover_simulation_not_found(self):
		"""
		Test if reader correctly peeks next line of
		input file to check if there is still content
		and fails.
		"""

		filename = TestReaderHasRoverSim.file_path + "test_2_line_file.txt"

		with reader.Reader(filename) as r:
			# read a couple of lines
			_ = r.file.readline()
			_ = r.file.readline()

			self.assertEqual(r.has_rover_simulation(), False)

if __name__ == "__main__":
	unittest.main(exit=False)