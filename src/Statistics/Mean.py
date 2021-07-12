from src.Calculator.Addition import addition
from src.Calculator.Division import division


def get_mean(data):
    try:
        num_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(num_values, total)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("ERROR!  That is an empty array.  Try again")