from rover_project import rover
import unittest

class TestRoverGetPosition(unittest.TestCase):
	""" Test Class for Rover.get_position method at rover module."""

	def test_get_position(self):
		"""
		Test if rover gets current position tuple correctly.
		"""

		pos_input = (10, 30, 'N')
		r = rover.Rover(pos_input)

		self.assertEqual(r.get_position(), pos_input)

if __name__ == "__main__":
	unittest.main(exit=False)