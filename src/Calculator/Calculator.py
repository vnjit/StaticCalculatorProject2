from src.Calculator.Addition import addition


class Calculator:
    result = 0

    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result