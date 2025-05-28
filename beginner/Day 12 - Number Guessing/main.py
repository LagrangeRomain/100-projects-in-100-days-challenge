import random
import art

EASY_DIFFICULTY_LIVES = 10
HARD_DIFFICULTY_LIVES = 5

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
    if difficulty == 'easy':
        return EASY_DIFFICULTY_LIVES
    else:
        return HARD_DIFFICULTY_LIVES

def check_guess(actual_guess, actual_answer, actual_lives):
    if actual_guess > actual_answer:
        print("Too High.")
        return actual_lives - 1
    elif actual_guess < actual_answer:
        print("Too Low.")
        return actual_lives - 1
    elif actual_guess == actual_answer:
        print(f"You got it! The answer was {actual_answer}.")
        return actual_lives
    return actual_lives


def game():
    random_answer = random.randint(1, 100)

    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    lives = set_difficulty()
    guess = 0
    while guess != random_answer and lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        lives = check_guess(guess, random_answer, lives)
    if lives == 0:
        print(f"You Lose! The answer was {random_answer}.")

game()
