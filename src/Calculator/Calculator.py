from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Multiplication import multiplication
from src.Calculator.Division import division
from src.Calculator.Square import square
from src.Calculator.SquareRoot import squareRoot

class Calculator:
    result = 0

    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    # Division
    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    # Square
    def square(self, a):
        self.result = square(a)
        return self.result

    # SquareRoot
    def squareroot(self, a):
        self.result = squareRoot(a)
        return self.result