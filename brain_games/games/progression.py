import random

RULES = 'What number is missing in the progression?'


def generate_progression(start, step, count):
    stack = []
    for index in range(count):
        current_element = start + index * step
        stack.append(current_element)
    return stack


def generate_round():
    start = random.randint(1, 25)
    step = random.randint(1, 5)
    count = random.randint(9, 14)

    stack = generate_progression(start, step, count)
    remove_numb = random.randrange(count)
    correct_answer = stack[remove_numb]
    stack[remove_numb] = '..'
    return stack, correct_answer
