import unittest

from basics.oop.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_add_strings(self):
        self.assertEqual(False, self.calculator.sum("1", "test"))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
