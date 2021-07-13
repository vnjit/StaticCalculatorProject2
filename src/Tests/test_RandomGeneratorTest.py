import unittest
from pprint import pprint
from src.RandomGenerator.RandomGenerator import RandomGenerator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = RandomGenerator()
        self.start = 1
        self.end = 100
        self.length = 3
        self.seed = 5
        self.num_val = 3

    def test_instantiate_calculator_self(self):
        self.assertIsInstance(self.random, RandomGenerator)


    def test_random_without_integer(self):
        int_random = self.random.random_without_integer(self.start, self.end)
        pprint(int_random)
        self.assertEqual(isinstance(self.random.random_without_integer(self.start, self.end), int), True)

    def test_random_without_decimal(self):
        decimal_random = self.random.random_without_decimal(self.start, self.end)
        pprint(decimal_random)
        self.assertEqual(isinstance(self.random.random_without_decimal(self.start, self.end), float), True)

    def test_random_with_integer(self):
        int_rd_seed = self.random.random_with_integer(self.start, self.end, self.seed)
        self.assertEqual(self.random.random_with_integer(self.start, self.end, self.seed), int_rd_seed)

    def test_random_integer_list(self):
        int_array = self.random.random_with_list_integer(self.start, self.end, self.length, self.seed)
        pprint(int_array)
        for val in int_array:
            test_value = int(val)
            self.assertEqual(isinstance(test_value, int), True)

    def test_random_decimal_list(self):
        decimal_array = self.random.random_with_list_decimal(self.start, self.end, self.length, self.seed)
        pprint(decimal_array)
        for val in decimal_array:
            test_value = float(val)
            self.assertEqual(isinstance(test_value, float), True)
