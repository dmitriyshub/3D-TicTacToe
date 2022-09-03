import random
import threading
import sched, time

s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    print("Doing stuff...")
    # do your stuff
    sc.enter(1, 1, do_something, (sc,))

s.enter(1, 1, do_something, (s,))
s.run()





def define_players():
    """
    this function ask for player names and make a random choice
    :return: player_choice variable - player name
    """
    player_a, player_b = input("Player one name?"), input("Player two name?")
    return player_a, player_b

def random_players(player_a,player_b):
    """
    This function choose a random player
    :param player_a: name of player 1
    :param player_b: name of player 2
    :return: first player to play
    """
    first_player = random.choice([player_a, player_b])
    if first_player == player_a:
        second_player = player_b
    else:
        second_player = player_a
    return first_player, second_player

def turn_check(turn):
    if turn % 2 == 0:
        return first_player
    else:
        return second_player

def choice_and_check():
    """
    This function choose
    :return:
    """
    while True:
        # Input from user
        board_choice, square_choice = input("Which board (1-3) ? "), input("Which square (1-9)? ")

        if not (board_choice.isdigit() or square_choice.isdigit()):
            print("Need to be a number")
            continue

        elif (board_choice.isdigit and (1 > int(board_choice)) > 3) or (square_choice.isdigit and (1 > int(square_choice.isdigit() > 9))):
            print(" not a valid range")
            continue

        else:
            return board_choice, square_choice



