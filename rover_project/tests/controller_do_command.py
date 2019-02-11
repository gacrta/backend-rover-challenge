from rover_project import controller, rover, reader
import unittest

class TestControllerDoCommand(unittest.TestCase):
	""" Test Class for Controller.do_command method at controller module."""

	file_path = 'rover_project/tests/'

	def init_controller_for_test(self):
		"""
		(TestControllerDoCommand) -> Controller

		TestControllerDoCommand auxiliar method to avoid duplicate of code.
		This inits x_limit and y_limit to 5.
		"""
		filename = TestControllerDoCommand.file_path + "test_real_input.txt"

		c = controller.Controller(filename)

		with reader.Reader(c.filename) as r:
			c.x_limit, c.y_limit = r.read_upper_right_coordinates()

		return c

	def test_controller_ok_move_foward_east(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 5, 'E')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (5, 5, 'E')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_nok_move_foward_east(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (5, 5, 'E')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (5, 5, 'E')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_ok_move_foward_south(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 1, 'S')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (4, 0, 'S')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_nok_move_foward_south(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 0, 'S')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (4, 0, 'S')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_ok_move_foward_west(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (1, 5, 'W')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (0, 5, 'W')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_nok_move_foward_west(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (0, 5, 'W')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (0, 5, 'W')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_ok_move_foward_north(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 4, 'N')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (4, 5, 'N')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_nok_move_foward_north(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 5, 'N')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'M')
		expected = (4, 5, 'N')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_turn_right(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 5, 'E')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'R')
		expected = (4, 5, 'S')

		self.assertEqual(a_rover.get_position(), expected)

	def test_controller_turn_left(self):
		"""
		Test if Controller can init reader instance correctly.
		"""

		ctrl = self.init_controller_for_test()
		pos = (4, 5, 'E')
		a_rover = rover.Rover(pos)
		ctrl.do_command(a_rover, 'L')
		expected = (4, 5, 'N')

		self.assertEqual(a_rover.get_position(), expected)

if __name__ == "__main__":
	unittest.main(exit=False)