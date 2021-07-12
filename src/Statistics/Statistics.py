from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import get_mean
from src.Statistics.Mean import get_median


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = get_mean(data)
        return self.result

    def median(self, data):
        self.result = get_median(data)
        return self.result