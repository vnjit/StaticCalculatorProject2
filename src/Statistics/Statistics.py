from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result