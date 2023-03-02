def function1(puzzle):
    # return all the possible actions in given state (puzzle)
    if puzzle.index(0) == 0:
        return ['<', '^']
    elif puzzle.index(0) == 1:
        return ['>', '<', '^']
    elif puzzle.index(0) == 2:
        return ['>', '^']
    elif puzzle.index(0) == 3:
        return ['<', '^', 'v']
    elif puzzle.index(0) == 4:
        return ['>', '<', '^', 'v']
    elif puzzle.index(0) == 5:
        return ['>', '^', 'v']
    elif puzzle.index(0) == 6:
        return ['<', 'v']
    elif puzzle.index(0) == 7:
        return ['>', '<', 'v']
    elif puzzle.index(0) == 8:
        return ['>', 'v']


def function2(selected_move, puzzle):
    # apply the action to the given state and return the new state

    # find index of zero in list
    index = puzzle.index(0)

    if selected_move == '>':
        puzzle[index] = puzzle[index - 1]
        puzzle[index - 1] = 0

    elif selected_move == '<':
        puzzle[index] = puzzle[index + 1]
        puzzle[index + 1] = 0

    elif selected_move == '^':
        puzzle[index] = puzzle[index - 3]
        puzzle[index - 3] = 0

    elif selected_move == 'v':
        puzzle[index] = puzzle[index + 3]
        puzzle[index + 3] = 0

    return puzzle


def function3(puzzle):
    # if puzzle is solved (in the correct order) return True, otherwise return False
    if puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 0]:
        return True
    else:
        return False
