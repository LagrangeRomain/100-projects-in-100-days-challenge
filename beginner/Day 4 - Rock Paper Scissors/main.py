import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

player_choice = game[int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))]
print(player_choice)

computer_choice = random.choice(game)
print(f"Computer chose:\n{computer_choice}")

if player_choice == computer_choice:
    print("It's a draw!")
elif (player_choice == rock and computer_choice == scissors) or \
     (player_choice == paper and computer_choice == rock) or \
     (player_choice == scissors and computer_choice == paper):
    print("You win")
else:
    print("You lose")