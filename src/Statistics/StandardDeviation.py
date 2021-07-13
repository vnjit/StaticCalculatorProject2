from src.Statistics.Variance import get_variance
from src.Calculator.SquareRoot import squareRoot


def get_standard_deviation(data):
    try:
        value = get_variance(data)
        return round(squareRoot(value),1)
    except ValueError:
        print("ERROR!  That is an empty array.  Try again.")