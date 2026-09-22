import math
import random

RULES = "Find the greatest common divisor of given numbers."


def generate_round():
    random_numb_first = random.randint(1, 100)
    random_numb_second = random.randint(1, 100)
    correct_answer = math.gcd(random_numb_first, random_numb_second)
    expression = f"{random_numb_first} {random_numb_second}"
    return expression, correct_answer
