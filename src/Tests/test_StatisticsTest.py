import unittest
from src.Statistics.Statistics import Statistics
from src.CsvReader.CsvReader import CsvReader
from src.Properties.Variable import S_Variable
from numpy import var, std

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.test_stat_data = CsvReader(S_Variable.Test_Static).data
        self.testData = [int(row['Value']) for row in self.test_stat_data]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        self.assertEqual(self.statistics.mean(self.testData),5.0625)

    def test_median_calculator(self):
        self.assertEqual(self.statistics.median(self.testData),5)

    def test_mode_calculator(self):
        self.assertEqual(self.statistics.mode(self.testData), 5)

    def test_variance_method(self):
        variance = (var(self.testData))
        self.assertEqual(self.statistics.variance(self.testData), 4.125)

    def test_standard_deviation(self):
        standard_deviation = (std(self.testData))
        self.assertAlmostEqual(self.statistics.standard_deviation(self.testData), 2.0)


if __name__ == '__main__':
    unittest.main()
