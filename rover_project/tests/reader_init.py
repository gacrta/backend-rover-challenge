from rover_project import reader
import unittest

class TestReader(unittest.TestCase):
	""" Test Class for Reader.__init__ method at reader module."""

	def test_reader_filename(self):
		"""
		Test if reader receives the correct filename.
		"""

		filename = "filename.txt"
		r = reader.Reader(filename)

		self.assertEqual(r.filename, filename)

	def test_reader_file(self):
		"""
		Test if reader inits file variable with None
		"""

		r = reader.Reader('')

		self.assertIsNone(r.file)

if __name__ == "__main__":
	unittest.main(exit=False)