import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calc_score(list_of_cards):
    if sum(list_of_cards) == 21 and len(list_of_cards) == 2:
        return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
        list_of_cards.remove(11)
        list_of_cards.append(1)

    return sum(list_of_cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You've lost, dealer has blackjack"
    elif user_score > 21:
        return "Bust! You went over"
    elif computer_score > 21:
        return "Dealer bust... You win!"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calc_score(user_cards)
        computer_score = calc_score(computer_cards)

        print(f"Your cards are {user_cards}, value: {user_score}")
        print(f"The dealer's face card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input("Would you like to get another card? y or n")
            if deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calc_score(computer_cards)

    print(f"Dealer hand {computer_cards}, with value {computer_score}")
    print(f"Player hand is {user_cards} with value {user_score}")

    print(compare(user_score, computer_score))


while input("Again? y or n") == "y":
    print("000" * 30)
    play_game()
