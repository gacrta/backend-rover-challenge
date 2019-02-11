from rover_project import rover
import unittest

class TestRover(unittest.TestCase):
	""" Test Class for Rover.__init__ method at rover module."""

	file_path = 'rover_project/tests/'

	def test_rover_x(self):
		"""
		Test if rover stores x value correctly.
		"""

		pos = (10, 30, 'A')
		r = rover.Rover(pos)

		self.assertEqual(r.x, 10)

	def test_rover_y(self):
		"""
		Test if rover stores y value correctly.
		"""

		pos = (10, 30, 'A')
		r = rover.Rover(pos)

		self.assertEqual(r.y, 30)

	def test_rover_direction(self):
		"""
		Test if rover stores direction value correctly.
		"""

		pos = (10, 30, 'A')
		r = rover.Rover(pos)

		self.assertEqual(r.direction, 'A')

if __name__ == "__main__":
	unittest.main(exit=False)