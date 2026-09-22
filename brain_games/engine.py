import prompt

from brain_games.cli import welcome_user

ROUNDS = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(game.RULES)

    for _ in range(ROUNDS):
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")

            print(f"Let's play again, {name}!")
            return
    print(f'Congratulations, {name}!')

