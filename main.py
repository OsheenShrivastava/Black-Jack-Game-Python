############### Blackjack Project #####################

# Difficulty Normal : Use all Hints below to complete the project.
# Difficulty Hard : Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard : Only use Hints 1 & 2 to complete the project.
# Difficulty Expert : Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card()

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10)
# and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21,
# remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the
# user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes,
# then use the deal_card() function to add another card to the user_cards List. If no, then
# the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in
# Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep
# drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If
# the computer and user both have the same score, then it's a draw. If the computer has a
# blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the
# user_score is over 21, then the user loses. If the computer_score is over 21, then the computer
# loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console
# and start a new game of blackjack and show the logo from art.py.

# Bug fix. If you and the computer are both over, you lose.
###########################################################################################

from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(U_Score, C_Score):
    if U_Score == C_Score:
        return "Draw"
    elif C_Score == 0:
        return "Lose, opponent has Blackjack"
    elif U_Score == 0:
        return "Win with a Blackjack"
    elif U_Score > 21:
        return "You went over. You lose."
    elif C_Score > 21:
        return "Opponent went over. You win."
    elif U_Score > C_Score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    User_Cards = []
    Computer_Cards = []
    User_Score = -1
    Computer_Score = -1
    is_game_over = False

    for card in range(2):
        User_Cards.append(deal_card())
        Computer_Cards.append(deal_card())

    while not is_game_over:
        User_Score = calculate_score(User_Cards)
        Computer_Score = calculate_score(Computer_Cards)

        print(f"Your cards: {User_Cards}, current score: {User_Score}")
        print(f"Computer's first card: {Computer_Cards[0]}")

        if User_Score == 0 or Computer_Score == 0 or User_Score > 21:
            is_game_over = True
        else:
            user_should_deal = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                User_Cards.append(deal_card())
            else:
                is_game_over = True

    while Computer_Score != 0 and Computer_Score < 17:
        Computer_Cards.append((deal_card()))
        Computer_Score = calculate_score(Computer_Cards)

    print(f"Your final hand: {User_Cards}, final score: {User_Score}")
    print(f"Computer's final hand: {Computer_Cards}, final score: {Computer_Score}")
    print(compare(User_Score, Computer_Score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()