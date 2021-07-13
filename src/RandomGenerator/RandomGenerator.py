from src.RandomGenerator.RGwithoutDecimal import random_without_decimal
from src.RandomGenerator.RGwithoutInteger import random_without_integer
from src.RandomGenerator.RGwithDecimal import random_with_decimal
from src.RandomGenerator.RGwithInteger import random_with_integer
from src.RandomGenerator.RGwithListInteger import random_with_list_integer
from src.RandomGenerator.RGwithListDecimal import random_with_list_decimal


class Random:
    result = 0


    def random_without_decimal(self, start, end):
        self.result = random_without_decimal(start, end)
        return self.result


    def random_without_integer(self, start, end):
        self.result = random_without_integer(start, end)
        return self.result


    def random_with_decimal(self, start, end, seed):
        self.result = random_with_decimal(start, end, seed)
        return self.result


    def random_with_integer(self, start, end, seed):
        self.result = random_with_integer(start, end, seed)
        return self.result

    def random_with_list_decimal(self, start, end, length, seed):
        self.result = random_with_list_decimal(start, end, length, seed)
        return self.result

    def random_with_list_integer(self, start, end, length, seed):
        self.result = random_with_list_integer(start, end, length, seed)
        return self.result