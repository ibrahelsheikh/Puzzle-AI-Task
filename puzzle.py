"""
Puzzle Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from functions import *


def print_puzzle(puzzle):
    p = ''
    for i in puzzle:
        if i == 0:
            p += ' '
        else:
            p += str(i)
    print(
        '-' * 13 + '\n' +
        '| ' + p[0] + ' | ' + p[1] + ' | ' + p[2] + ' |' + '\n' +
        '-' * 13 + '\n' +
        '| ' + p[3] + ' | ' + p[4] + ' | ' + p[5] + ' |' + '\n' +
        '-' * 13 + '\n' +
        '| ' + p[6] + ' | ' + p[7] + ' | ' + p[8] + ' |' + '\n' +
        '-' * 13 + '\n'
    )


def human_play(puzzle):
    while True:
        print_puzzle(puzzle)
        available_move = available_movement(puzzle)
        print('available_move: ', available_move)
        selected_move = input('Select a move: ')
        if selected_move not in available_move:
            print('Game Over');
            break

        puzzle = apply_move(selected_move, puzzle)
        if check_final_state(puzzle):
            print_puzzle(puzzle)
            print('You Win');
            break

    puzzle = apply_move(puzzle, selected_move)
    print_puzzle(puzzle)


if __name__ == '__main__':
    puzzle = [
        3, 1, 2,
        4, 0, 5,
        6, 7, 8
    ]
    human_play(puzzle)


