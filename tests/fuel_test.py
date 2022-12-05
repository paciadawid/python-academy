import unittest

from basics.oop.calculate_fuel import calculate_fuel


class MyTestCase(unittest.TestCase):

    def test_12(self):
        self.assertEqual(2, calculate_fuel(12))

    def test_negative_value(self):
        self.assertEqual(False, calculate_fuel(-1))

    def test_zero(self):
        self.assertEqual(False, calculate_fuel(0))

    def test_string(self):
        self.assertEqual(False, calculate_fuel("test"))

    def test_multiple_input(self):
        self.assertEqual(False, calculate_fuel(1, 2))

    def test_value_min_positive(self):
        self.assertEqual(1, calculate_fuel(1))

    def test_float(self):
        self.assertEqual(2, calculate_fuel(12.5))


if __name__ == '__main__':
    unittest.main()
