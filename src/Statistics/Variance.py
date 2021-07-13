from src.Statistics.Mean import get_mean
from src.Calculator.Division import division
from src.Calculator.Addition import addition
from src.Calculator.Square import square
from src.Calculator.Subtraction import subtraction


def get_variance(data):
    x1 = get_mean(data)
    num_values = len(data)
    total = 0
    total1 = 0
    data1 = []
    for i in range(0, len(data)):
        a = data[i - 1]
        total_sum = subtraction(a, x1)
        total = square(total_sum)
        data1.append(total)
    for i in range(0, len(data1)):
        total1 = total1 + addition(0, data1[i])
    return round(division(num_values - 1, total1), 1)