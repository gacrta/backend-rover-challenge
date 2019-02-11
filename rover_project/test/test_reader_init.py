from rover_project import reader
import unittest

class TestReader(unittest.TestCase):
	""" Test Class for Reader.__init__ method at reader module."""

	file_path = 'rover_project/tests/'

	def test_reader_valid_filename(self):
		"""
		Test if reader can open a file correctly.
		"""

		filename = TestReader.file_path + "test_init_filename.txt"

		with reader.Reader(filename) as r:
			pass

		self.assertIsNotNone(r.file)

	def test_reader_not_valid_file(self):
		"""
		Test if reader raises FileNotFoundError exception when tries
		to open non existing file
		"""

		self.assertRaises(FileNotFoundError, reader.Reader, '')

if __name__ == "__main__":
	unittest.main(exit=False)