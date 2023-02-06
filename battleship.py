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

    try:
        # user selects game mode, if invalid entry rerun prompt)
        game_mode_selection = input("""\nPlease select a game mode:\n(1) Play against AI\n(2) Play against human (COMING SOON)\n""")
        if int(game_mode_selection) == 1:
            return 'ai'
        elif int(game_mode_selection) == 2:
            return 'human'
        else:
            clear()
            print("Please select a valid number entry!")
            user_selects_game_mode()
    except KeyboardInterrupt:
        # user manually exited game
        sys.exit(0)
    except:
        # invalid user input (random text, unsupported number, etc) so re-run game selection prompt
        clear()
        print("Please select a valid number entry!")
        user_selects_game_mode()


if __name__ == "__main__":
    clear()
    print("Welcome to Battleship!")
    game_mode = user_selects_game_mode()

    clear()
    board = board.BoardManager(10)
    print(board.add_ship(1, 0, 3, hor=True))
    print(board.add_ship(1, 2, 5, hor=True))
    print(board.add_ship(8, 3, 3, hor=False))
    print(board.add_ship(2, 4, 2, hor=False))
    print(board.add_ship(4, 5, 4, hor=False))
    print(board.add_ship(1, 0, 3, hor=False))
    print(DataFrame(board.board))
