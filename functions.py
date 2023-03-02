def function1(puzzle):
    # return all the possible actions in given state (puzzle)
    if puzzle[0] == 0:
        return ['<', '^']
    elif puzzle[2] == 0:
        return ['>', '^']
    elif puzzle[3] == 0:
        return ['<', '^', 'v']
    elif puzzle[4] == 0:
        return ['<', '>', '^', 'v']
    elif puzzle[5] == 0:
        return ['>', '^', 'v']
    elif puzzle[6] == 0:
        return ['<', 'v']
    elif puzzle[8] == 0:
        return ['>', 'v']


def function2(selected_move, puzzle):
    # apply the action to the given state and return the new state

    # find index of zero in list
    index = puzzle.index(0)

    if selected_move == '<':
        puzzle[index] = puzzle[index - 1]
        puzzle[index - 1] = 0

    elif selected_move == '>':
        puzzle[index] = puzzle[index + 1]
        puzzle[index + 1] = 0

    elif selected_move == '^':
        puzzle[index] = puzzle[index - 3]
        puzzle[index - 3] = 0

    elif selected_move == 'v':
        puzzle[index] = puzzle[index + 3]
        puzzle[index + 3] = 0


def function3(puzzle):
    # if puzzle is solved (in the correct order) return True, otherwise return False
    if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True
    else:
        return False
    pass
