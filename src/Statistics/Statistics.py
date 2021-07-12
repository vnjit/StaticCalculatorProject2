from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import get_mean


class Statistics(Calculator):

    def mean(self, data):
        self.result = get_mean(data)
        return self.result