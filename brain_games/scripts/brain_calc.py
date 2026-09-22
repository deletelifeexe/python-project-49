import operator
import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


OPS = {"*": operator.mul,
       "+": operator.add,
       "-": operator.sub}


def brain_calc(name):
    count_win_answers = 0

    print('What is the result of the expression?')

    while count_win_answers != 3:

        random_numb_first = random.randint(1, 100)
        random_numb_second = random.randint(1, 100)
        random_sign = random.choice(list(OPS.keys()))

        expression = f'{random_numb_first} {random_sign} {random_numb_second}'
        print(f"Question: {expression}")
        result = OPS[random_sign](random_numb_first, random_numb_second)

        answer = prompt.integer('Your answer: ')
        if answer == result:
            count_win_answers += 1
            print('Correct!')

        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    brain_calc(name)


if __name__ == "__main__":
    main()



