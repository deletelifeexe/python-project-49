import operator
import random

RULES = "What is the result of the expression"

OPS = {"*": operator.mul,
       "+": operator.add,
       "-": operator.sub}


def generate_round():
    random_numb_first = random.randint(1, 100)
    random_numb_second = random.randint(1, 100)
    random_sign = random.choice(list(OPS.keys()))
    expression = f"{random_numb_first} {random_sign} {random_numb_second}"
    correct_answer = OPS[random_sign](random_numb_first, random_numb_second)
    return expression, correct_answer
