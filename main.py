from board import *
from functions import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    player_a, player_b = define_players()
    player_a, player_b = random_players(player_a, player_b)

    print(print_tic_tac_toe())
    print(print_scoreboard())



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
