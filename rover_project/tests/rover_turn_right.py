from rover_project import rover
import unittest

class TestTurnRight(unittest.TestCase):
	""" Test Class for Rover.turn_right method at rover module."""

	def test_rover_turn_right_when_facing_north(self):
		"""
		Test if rover can turn right when facing North direction.
		"""

		initial_pos = (3, 4, 'N')
		r = rover.Rover(initial_pos)
		r.turn_right()
		pos = (r.x, r.y, r.direction)
		expected = (3, 4, 'E')

		self.assertEqual(pos, expected)

	def test_rover_turn_right_when_facing_east(self):
		"""
		Test if rover can turn right when facing East direction.
		"""

		initial_pos = (3, 4, 'E')
		r = rover.Rover(initial_pos)
		r.turn_right()
		pos = (r.x, r.y, r.direction)
		expected = (3, 4, 'S')

		self.assertEqual(pos, expected)

	def test_rover_turn_right_when_facing_south(self):
		"""
		Test if rover can turn right foward when facing South direction.
		"""

		initial_pos = (3, 4, 'S')
		r = rover.Rover(initial_pos)
		r.turn_right()
		pos = (r.x, r.y, r.direction)
		expected = (3, 4, 'W')

		self.assertEqual(pos, expected)

	def test_rover_turn_right_when_facing_west(self):
		"""
		Test if rover can turn right when facing West direction.
		"""

		initial_pos = (3, 4, 'W')
		r = rover.Rover(initial_pos)
		r.turn_right()
		pos = (r.x, r.y, r.direction)
		expected = (3, 4, 'N')

		self.assertEqual(pos, expected)

	

	

if __name__ == "__main__":
	unittest.main(exit=False)