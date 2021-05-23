
import random
from art import logo


def deal_card():  # randomly chooses a card from the list
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:  # if user is having 10 and 11
        return 0  # 0 is tagged to game over in subsequent codes
    if 11 in cards and sum(cards) > 21:  # if third card is an ace and total score > 21
        cards.remove(11)
        cards.append(1)  # treat ace as 1 and not 11
    return sum(cards)


def compare_score(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "You lose, opponent has BlackJack 😱"
    elif u_score == 0:
        return "You win with a BlackJack 😎"
    elif u_score > 21:
        return "You went over, you lose 😰"
    elif c_score > 21:
        return "Opponent went over, you win 🤓"
    elif u_score > c_score:
        return "You win with a higher score 😁"
    else:
        return "Opponent has a higher score, you lose 😨"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):  # picks up 2 cards each for user and computer
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    is_game_over = False
    while not is_game_over:
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            print("Your cards : {0}, Current Score : {1}".format(user_cards, user_score))
            print("Computer's first card : {}".format(computer_cards[0]))  # print only the first card
            response = input("Type 'yes' or 'y' to get another card, type 'n' to pass. \n : ")
            if response == 'y' or response == 'yes':
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("Your final hand {0}, and final score {1}".format(user_cards, user_score))
    print("Computer's final hand {0} and final score {1}".format(computer_cards, computer_score))
    print(compare_score(user_score, computer_score))


while input("Do you want to play the game of BlackJack? Type 'y' or 'n'. \n : ") == 'y' or 'yes':
    play_game()
