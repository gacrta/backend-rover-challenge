from rover_project import controller
import unittest

class TestControllerFormatPosition(unittest.TestCase):
	""" Test Class for Controller.format_position method at controller module."""

	def test_controller_test_one(self):
		"""
		Test if Controller can format position correctly.
		"""

		c = controller.Controller("")

		pos = (1, 4, 'N')
		result = c.format_position(pos)
		expected = "1 4 N"

		self.assertEqual(result, expected)

	def test_controller_test_two(self):
		"""
		Test if Controller can format position correctly.
		"""

		c = controller.Controller("")

		pos = (7, 0, 'W')
		result = c.format_position(pos)
		expected = "7 0 W"

		self.assertEqual(result, expected)

if __name__ == "__main__":
	unittest.main(exit=False)