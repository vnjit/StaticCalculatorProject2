from src.Calculator.Calculator import Calculator
from src.Statistics.Mean import get_mean
from src.Statistics.Median import get_median
from src.Statistics.Mode import get_mode


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

    def mode(self, data):
        self.result = get_mode(data)
        return self.result

