from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Division import division


def get_median(data):
    try:
        num_values = len(data)
        data.sort()
        if num_values % 2 == 0:
            value1 = data[int(division(2, num_values))]
            value2 = data[int(subtraction(division(2, num_values)), 1)]
            result = division(2, addition(value1, value2))
        else:
            result = data[int(division(2, num_values))]

            return result
    except ValueError:
            print("ERROR!  Data is Empty.  Try again.")



