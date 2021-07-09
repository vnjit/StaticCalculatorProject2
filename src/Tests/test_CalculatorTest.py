import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.CsvReader import CsvReader

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.mainCalculator = MainCalculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.mainCalculator, MainCalculator)

        # Unit Test for Addition

    def test_addition(self):
        test_add_data = CSVReader(StaticVariable.unitTestAddition).data
        for row in test_add_data:
            self.assertEqual(self.mainCalculator.add(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.mainCalculator.result, int(row[StaticVariable.result]))


if __name__ == '__main__':
    unittest.main()
