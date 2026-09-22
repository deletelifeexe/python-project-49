import math
import random

RULES = "Find the greatest common divisor of given numbers."

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    random_numb_first = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_numb_second = random.randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = math.gcd(random_numb_first, random_numb_second)
    expression = f"{random_numb_first} {random_numb_second}"
    return expression, correct_answer
