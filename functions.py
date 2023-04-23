def get_actions(puzzle):
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


def get_state(selected_move, puzzle):
    # apply the action to the given state and return the new state
    puzzle_copy = puzzle[:]

    # find index of zero in list
    index = puzzle_copy.index(0)

    if selected_move == '>':
        puzzle_copy[index] = puzzle_copy[index + 1]
        puzzle_copy[index + 1] = 0

    elif selected_move == '<':
        puzzle_copy[index] = puzzle_copy[index - 1]
        puzzle_copy[index - 1] = 0

    elif selected_move == 'v':
        puzzle_copy[index] = puzzle_copy[index + 3]
        puzzle_copy[index + 3] = 0

    elif selected_move == '^':
        puzzle_copy[index] = puzzle_copy[index - 3]
        puzzle_copy[index - 3] = 0

    return puzzle_copy


def isgoal(puzzle):
    # if puzzle is solved (in the correct order) return True, otherwise return False
    return puzzle == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def compute_cost(action, param):
    return 1


def compute_heuristic(puzzle):
    count = 0
    for i in range(len(puzzle)):
        if puzzle[i] != i: count += 1
    return count