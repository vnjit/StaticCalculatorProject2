import unittest
from src.Calculator.Calculator import Calculator
from src.CsvReader.CsvReader import CsvReader
from src.Properties.Variable import S_Variable

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.Calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.Calculator, Calculator)

        # Test for Addition

    def test_addition(self):
        test_addition_data = CsvReader(S_Variable.Test_Addition).data
        for row in test_addition_data:
            self.assertEqual(self.Calculator.add(row[S_Variable.value1], row[S_Variable.value2]),
                             int(row[S_Variable.result]))
            self.assertEqual(self.Calculator.result, int(row[S_Variable.result]))

        # Test for Subtraction
    def test_subtraction(self):
        test_subtraction_data = CsvReader(S_Variable.Test_Subtraction).data
        for row in test_subtraction_data:
            self.assertEqual(self.Calculator.subtract(row[S_Variable.value1], row[S_Variable.value2]),
                             int(row[S_Variable.result]))
            self.assertEqual(self.Calculator.result, int(row[S_Variable.result]))

        # Test for Multiplication
    def test_multiplication(self):
        test_multiplication_data = CsvReader(S_Variable.Test_Multiplication).data
        for row in test_multiplication_data:
            self.assertEqual(self.Calculator.multiply(row[S_Variable.value1], row[S_Variable.value2]),
                             int(row[S_Variable.result]))
            self.assertEqual(self.Calculator.result, int(row[S_Variable.result]))

        # Test for Division
    def test_division(self):
        test_division_data = CsvReader(S_Variable.Test_Division).data
        for row in test_division_data:
            self.assertAlmostEqual(self.Calculator.divide(row[S_Variable.value1], row[S_Variable.value2]),
                                   float(row[S_Variable.result]))
            self.assertAlmostEqual(self.Calculator.result, float(row[S_Variable.result]))

        # Test for Square
    def test_square(self):
        test_square_data = CsvReader(S_Variable.Test_Square).data
        for row in test_square_data:
            self.assertAlmostEqual(self.Calculator.square(row[S_Variable.value1]), float(row[S_Variable.result]))
            self.assertAlmostEqual(self.Calculator.result, float(row[S_Variable.result]))

        # Test for SquareRoot
    def test_squareRoot(self):
        test_squareRoot_data = CsvReader(S_Variable.Test_SquareRoot).data
        for row in test_squareRoot_data:
            self.assertAlmostEqual(self.Calculator.squareroot(row[S_Variable.value1]), float(row[S_Variable.result]))
            self.assertAlmostEqual(self.Calculator.result, float(row[S_Variable.result]))

if __name__ == '__main__':
    unittest.main()
