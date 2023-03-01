"""
8Puzzle Game
-------------
| 0 | 1 | 2 |
-------------
| 3 | 4 | 5 |
-------------
| 6 | 7 | 8 |
-------------
"""

from puzzle_functions import *
import random
import AiSearch


def print_puzzle(puzzle):
    s = ""
    for cell in puzzle:
        if cell != 0:
            s += str(cell)
        else:
            s += ' '
    print(
        '-' * 13 + '\n' +
        '| ' + s[0] + ' | ' + s[1] + ' | ' + s[2] + ' |' + '\n' +
        '-' * 13 + '\n' +
        '| ' + s[3] + ' | ' + s[4] + ' | ' + s[5] + ' |' + '\n' +
        '-' * 13 + '\n' +
        '| ' + s[6] + ' | ' + s[7] + ' | ' + s[8] + ' |' + '\n' +
        '-' * 13
    )


def shuffle(n):
    puzzle = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for _ in range(n):
        actions = generate_actions(puzzle)
        rand_index = random.randint(0, len(actions) - 1)
        puzzle = apply_action(puzzle, actions[rand_index])
    return puzzle


def human_solve(puzzle):
    puzzle = puzzle[:]
    while (True):
        print_puzzle(puzzle)
        available_actions = generate_actions(puzzle)
        print('available actions: ' + ' , '.join(available_actions))
        action = input("your action:")
        if action not in available_actions:
            print('Game Over');
            return
        puzzle = apply_action(puzzle, action)
        if check_puzzle(puzzle):
            print_puzzle(puzzle);
            print("You win");
            return


def computer_solve(puzzle, strategy, h=None, flag=False):
    S = AiSearch.solve(strategy, puzzle, generate_actions, apply_action, check_puzzle, puzzle_cost, h)
    print(strategy)
    for i in S:
        print(i, ": ", S[i])
    print('-' * 50)
    if flag:
        puzzle = puzzle[:]
        print_puzzle(puzzle)
        for action in S['solution']:
            puzzle = apply_action(puzzle, action)
            print_puzzle(puzzle)


puzzle = shuffle(25)
# puzzle = [1, 7, 2, 3, 5, 0, 4, 6, 8]
# puzzle = [1, 0, 2, 6, 3, 5, 4, 7, 8] #DFS
# puzzle = [3, 2, 5, 6, 1, 8, 7, 0, 4] #Greedy not optimal
# puzzle = [2, 6, 5, 4, 8, 7, 3, 1, 0] #expanded_nodes :  42977
print_puzzle(puzzle)

# human_solve(puzzle)
# computer_solve(puzzle,'DFS')
# computer_solve(puzzle,'BFS')
computer_solve(puzzle, 'UCS')
computer_solve(puzzle, 'Greedy', h1)
computer_solve(puzzle, 'Greedy', h2)
computer_solve(puzzle, 'Astar', h1)
computer_solve(puzzle, 'Astar', h2)
