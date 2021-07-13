from src.Statistics.Mean import get_mean
from src.Calculator.Division import division
from src.Calculator.Square import square


def get_variance(data):
    try:
        x1 = get_mean(data)
        num_values = len(data)
        var = 0
        for i in data:
            var = var + square(i -  x1)
        result = division(num_values, var)
        return result

    except ValueError:
        print("ERROR: That is an emtpy array! Try again.")