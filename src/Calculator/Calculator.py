from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Multiplication import multiplication

class Calculator:
    result = 0

    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result