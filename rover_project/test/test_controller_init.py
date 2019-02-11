from rover_project import controller
import unittest

class TestController(unittest.TestCase):
	""" Test Class for Controller.__init__ method at controller module."""

	file_path = 'rover_project/tests/'

	def test_controller_valid_filename(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		filename = TestController.file_path + "test_real_input.txt"

		c = controller.Controller(filename)

		self.assertIsNotNone(c.reader.file)

	def test_controller_not_valid_file(self):
		"""
		Test if Controller raises FileNotFoundError exception when tries
		to open non existing file
		"""

		self.assertRaises(FileNotFoundError, controller.Controller, '')

if __name__ == "__main__":
	unittest.main(exit=False)