import os
import sys

from pandas import DataFrame

import board


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def user_selects_game_mode():
    game_modes = {
    1: 'Battleship against AI',
    2: 'Battleship against human'
    }

    # user selects game mode, if invalid entry rerun prompt)
    game_mode_selection = input("""\nPlease select a game mode:\n(1) Play against AI\n(2) Play against human (COMING SOON)\n(3) Quit\n""")

    # handle bad input (unsupported number, random text, etc) by re-running prompt
    if not game_mode_selection.isdigit():
        clear()
        print("Please select a valid number entry!")
        user_selects_game_mode()

    if int(game_mode_selection) == 1:
        return 'ai'
    elif int(game_mode_selection) == 2:
        return 'human'
    elif int(game_mode_selection) == 3:
        clear()
        sys.exit("Goodbye!")


if __name__ == "__main__":
    clear()
    print("Welcome to Battleship!")
    game_mode = user_selects_game_mode()

    clear()
    board = board.BoardManager(10)
    for i in range(5, -1, -1):
        board.add_ship(i)
        print(DataFrame(board.board))