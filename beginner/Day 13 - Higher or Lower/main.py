import random
import art
import game_data

def display_and_ask(person_1, person_2):
    print(f"Compare A: {person_1['name']}, a {person_1['description']}, from {person_1['country']}.")
    print(art.vs)
    print(f"Compare B: {person_2['name']}, a {person_2['description']}, from {person_2['country']}.")
    answer = ""
    while answer.lower() != "a" and answer.lower() != "b":
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer.lower() != "a" and answer.lower() != "b":
            print("Wrong input, try again.")
    return answer

def check_answer(person_1, person_2):
    return person_1['follower_count'] > person_2['follower_count']

def game_control(win, points, end_game):
    if win:
        points += 1
    else :
        end_game = True
    return points, end_game

def game(celebrity_a, score, game_over):
    celebrity_b = random.choice(game_data.data)

    user_answer = display_and_ask(celebrity_a, celebrity_b)

    if user_answer.lower() == 'a':
        has_won = check_answer(celebrity_a, celebrity_b)
    else:
        has_won = check_answer(celebrity_b, celebrity_a)

    score, game_over = game_control(has_won, score, game_over)

    if game_over:
        print(f"Sorry, that's wrong. Final score: {score}")
    else:
        print(f"You're right! Current score: {score}")
        celebrity_a = celebrity_b
    return celebrity_a, score, game_over

def main():
    print(art.logo)

    correct_answers = 0
    stop_game = False
    random_person = random.choice(game_data.data)

    while not stop_game:
        random_person, correct_answers, stop_game = game(random_person, correct_answers, stop_game)

main()