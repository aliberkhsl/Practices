def maze_solver(start, board, goal=(1, 0)):

    if goal in start:
        return [start]
    explored = set()
    frontier = [[start]]
    while frontier:
        path = frontier.pop(0)
        current = path[-1]

        for(state, action) in successors(current, board).items():

            if state not in explored:
                explored.add(state)

                path2 = path + [action, state]

                if goal == state:
                    return path2
                else:
                    frontier.append(path2)
    return Fail


Fail = []


def successors(current, board):

    return {((current[0], current[1] + 1) if ((len(board[0]) - 1) >= current[1] + 1 and board[current[0]][(current[1] + 1)] != '# ') else (current[0], current[1])): 'RIGHT',
            ((current[0], current[1] - 1) if (board[current[0]][current[1] - 1] != '#' and current[1] - 1 >= 0) else (current[0], current[1])): 'LEFT',
            ((current[0] - 1, current[1]) if (board[current[0] - 1][current[1]] != '#' and current[0] - 1 >= 0) else (current[0], current[1])): 'UP',
            ((current[0] + 1, current[1]) if ((len(board) - 1) >= current[0] + 1 and board[current[0] + 1][current[1]] != '#') else (current[0], current[1])): 'DOWN'}


board = [['#', '#', '#', '#', '#'], ['e', '-', '-', '#', '-'], ['-', '-', '-', '#',
                                                                '-'], ['-', '#', '#', '#', '-'], ['-', '-', '-', '-', '-']]  # example input format
current = (1, 4)  # start point
print maze_solver(current, board)
