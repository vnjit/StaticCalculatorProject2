from numpy import random
from src.RandomGenerator.RandomGenerator import random_without_decimal


def random_with_decimal(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rd_with_decimal = random_without_decimal(start, end)
        return rd_with_decimal
    finally:
        random.set_state(state)