import random

RULES = 'What number is missing in the progression?'

MIN_START = 1
MAX_START = 25
MIN_STEP = 1
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        progression.append(start + index * step)
    return progression


def generate_round():
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)
    length = random.randint(MIN_LENGTH, MAX_LENGTH)

    progression = generate_progression(start, step, length)
    hidden_index = random.randrange(length)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer
