import operator
import random

RULES = "What is the result of the expression"

MIN_NUMBER = 1
MAX_NUMBER = 100

OPS = {"*": operator.mul,
       "+": operator.add,
       "-": operator.sub}


def generate_round():
    random_numb_first = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_numb_second = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_sign = random.choice(list(OPS))
    expression = f"{random_numb_first} {random_sign} {random_numb_second}"
    correct_answer = OPS[random_sign](random_numb_first, random_numb_second)
    return expression, correct_answer
