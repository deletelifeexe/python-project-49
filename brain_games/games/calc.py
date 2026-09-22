import operator
import random

RULES = "What is the result of the expression?"

MIN_NUMBER = 1
MAX_NUMBER = 100

OPS = {"*": operator.mul,
       "+": operator.add,
       "-": operator.sub}


def generate_round():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    random_sign = random.choice(list(OPS))
    question = f"{first_number} {random_sign} {second_number}"
    correct_answer = OPS[random_sign](first_number, second_number)
    return question, correct_answer
