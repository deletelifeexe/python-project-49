import random

import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def parity_check(number):
    return 'yes' if number % 2 == 0 else 'no'


def brain_even(name):
    count_win_answers = 0
    print('Answer "yes" if the number is even, otherwise answer "no".')
    while count_win_answers != 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        correct = parity_check(random_number)
        answer = prompt.string('Your answer: ')
        if answer == correct:
            count_win_answers += 1
            print('Correct!')

        else:
            print(f"{answer} is wrong answer ;(. "
                  f"Correct answer is was {parity_check(random_number)}")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    brain_even(name)


if __name__ == "__main__":
    main()



