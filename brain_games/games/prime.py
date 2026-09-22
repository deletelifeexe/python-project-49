import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return 'no'
    for i in range(2, n):
        if n % i == 0:
            return 'no'
    return 'yes'


def generate_round():
    number = random.randint(1, 15)
    correct_answer = is_prime(number)
    return number, correct_answer