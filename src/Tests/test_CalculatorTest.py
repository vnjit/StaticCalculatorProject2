import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.CsvReader import CsvReader
from src.StaticProperties.StaticVariable import StaticVariable

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Calculator, Calculator)

        # Test for Addition

    def test_addition(self):
        test_add_data = CsvReader(StaticVariable.TestAddition).data
        for row in test_add_data:
            self.assertEqual(self.Calculator.add(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.Calculator.result, int(row[StaticVariable.result]))

        # Test for Subtraction
    def test_subtraction(self):
        test_sub_data = CsvReader(StaticVariable.TestSubtraction).data
        for row in test_sub_data:
            self.assertEqual(self.Calculator.sub(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.Calculator.result, int(row[StaticVariable.result]))

        # Test for Multiplication
    def test_multiplication(self):
        test_multiple_data = CsvReader(StaticVariable.TestMultiplication).data
        for row in test_multiple_data:
            self.assertEqual(self.Calculator.multiple(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.Calculator.result, int(row[StaticVariable.result]))

if __name__ == '__main__':
    unittest.main()
