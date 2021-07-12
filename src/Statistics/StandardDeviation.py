from Statistics.Variance import get_variance
from src.Calculator.SquareRoot import squareRoot


def get_standard_deviation(data):
    value = get_variance(data)
    return round(squareRoot(value),1)