def available_movement(puzzle):
    # return all the possible actions in given state (puzzle)
    if puzzle.index(0) == 0:
        return ['>', 'v']
    elif puzzle.index(0) == 1:
        return ['>', '<', 'v']
    elif puzzle.index(0) == 2:
        return ['<', 'v']
    elif puzzle.index(0) == 3:
        return ['>', 'v', '^']
    elif puzzle.index(0) == 4:
        return ['>', '<', '^', 'v']
    elif puzzle.index(0) == 5:
        return ['<', '^', 'v']
    elif puzzle.index(0) == 6:
        return ['>', '^']
    elif puzzle.index(0) == 7:
        return ['>', '<', '^']
    elif puzzle.index(0) == 8:
        return ['<', '^']

    """
    available_move = []
    if puzzle.index(0) < 6:
        available_move.append('^')
    if puzzle.index(0) > 2:
        available_move.append('v')
    if puzzle.index(0) % 3 != 0:
        available_move.append('>')
    if puzzle.index(0) % 3 != 2:
        available_move.append('<')
    return available_move
     """


def apply_move(selected_move, puzzle):
    # apply the action to the given state and return the new state

    # find index of zero in list
    index = puzzle.index(0)

    if selected_move == '>':
        puzzle[index] = puzzle[index + 1]
        puzzle[index + 1] = 0

    elif selected_move == '<':
        puzzle[index] = puzzle[index - 1]
        puzzle[index - 1] = 0

    elif selected_move == 'v':
        puzzle[index] = puzzle[index + 3]
        puzzle[index + 3] = 0

    elif selected_move == '^':
        puzzle[index] = puzzle[index - 3]
        puzzle[index - 3] = 0

    return puzzle


def check_final_state(puzzle):
    # if puzzle is solved (in the correct order) return True, otherwise return False
    if puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        return True
    else:
        return False
