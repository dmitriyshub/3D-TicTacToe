import random

def players():
    """
    this function ask for player names and make a random choice
    :return: player_choice variable - player name
    """
    player_a, player_b = input("Player one name?"), input("Player two name?")
    player_choice = random.choice([player_a, player_b])
    return player_choice


def choice():
    while True:
        # Input from user
        board_choice, square_choice = input("Which board (1-3) ? "), input("Which square (1-9)? ")

        if not (board_choice.isdigit() or square_choice.isdigit()):
            print("Need to be a number")
            continue

        if (board_choice.isdigit and (1 > int(board_choice)) > 3) or (square_choice.isdigit and (1 > int(square_choice.isdigit() > 9) )):
            print(" not a valid range")
            continue

        else:
            return board_choice, square_choice


choice()