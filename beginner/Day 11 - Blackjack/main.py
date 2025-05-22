import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_checker(hand):
    """Check if last card is an ace. If yes, choice between 1 and 11"""
    if hand[-1] == 11 and sum(hand) > 21:
        hand[-1] = 1
    return hand

def add_a_card(hand):
    """Add a card to hand"""
    hand.append(random.choice(cards))
    hand = ace_checker(hand)
    return hand

def print_score(hand1, hand2):
    """Print the scores"""
    print(f"    Your cards: {hand1}, current score: {sum(hand1)}")
    print(f"    Computer first card: {hand2[0]}")

def print_final_score(hand1, hand2):
    """Print the finals scores"""
    print(f"    Your final hand: {hand1}, final score: {sum(hand1)}")
    print(f"    Computer's final hand: {hand2}, final score: {sum(hand2)}")

def blackjack_game():
    """A game of blackjack"""
    player_hand = ace_checker([random.choice(cards),random.choice(cards)])
    computer_hand = ace_checker([random.choice(cards),random.choice(cards)])

    print_score(player_hand, computer_hand)

    hand_out_card = 'y'
    while hand_out_card == 'y' and sum(player_hand) < 22:
        hand_out_card= input("Type 'y' to get a card, type 'n' to pass: ")
        if hand_out_card == 'y':
            player_hand = add_a_card(player_hand)
        print_score(player_hand, computer_hand)

    if sum(player_hand) > 21:
        print_final_score(player_hand, computer_hand)
        print("You went over. You lose ! 😠")
    else:
        while sum(computer_hand) < 17:
            add_a_card(computer_hand)
        print_final_score(player_hand, computer_hand)
        if sum(player_hand) < sum(computer_hand) and sum(computer_hand) < 22:
            print("You lose! 😠")
        elif sum(player_hand) == sum(computer_hand):
            print("It's a draw! 😐")
        else:
            print("You win! 😃")


play = 'y'
while play == 'y':
    play = input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")
    if play == 'y':
        print("\n" * 20)
        print(art.logo)
        blackjack_game()