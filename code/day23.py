# aoc 2021 day 23 part 1
from math import inf
from itertools import product, chain

state = [[x for x in line] for line in open("../input/day23_test.txt").read().splitlines()]
state = [[(i, j, state[i][j]) for j in range(len(state[i]))] for i in range(len(state))]

state = {
    (i, j): v for (i, j, v) in [item for sublist in state for item in sublist]
}

cost_map = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}

room_map = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

# memoization, if needed
states_map = dict()


def map_to_str(s):
    grid = [[' ' for _ in range(13)] for _ in range(5)]
    for (i, j), v in s.items():
        grid[i][j] = v
    grid_str = '\n'.join(''.join(line) for line in grid)
    return grid_str


def possible(s, start, end):
    miny = min(start[1], end[1])
    maxy = max(start[1], end[1])
    hallway_move = product((1,), range(miny, maxy+1))
    minx = min(start[0], end[0])
    maxx = max(start[0], end[0])
    room_num = start[1] if start[0] != 1 else end[1]
    room_move = product(range(minx, maxx+1), (room_num,))
    if any(s[p] != '.' for p in chain(hallway_move, room_move) if p != start):
        return False  # can't jump over other piece
    else:  # return cost
        return True


def moves(s, pos):
    piece = s[pos]
    assert piece in ['A', 'B', 'C', 'D']
    if pos[0] == 1:  # standing in hallway, must move into room
        if s[3, room_map[piece]] == '.':  # room not occupied
            if possible(s, pos, (3, room_map[piece])):
                yield 3, room_map[piece]
        elif s[3, room_map[piece]] == piece and s[2, room_map[piece]] == '.':  # room occupied with correct amoeba
            if possible(s, pos, (2, room_map[piece])):
                yield 2, room_map[piece]
    else:  # standing in a room
        # if we're in the incorrect room or if the room is incomplete
        if pos[1] != room_map[piece] or (s[(2, pos[1])] != s[(3, pos[1])]):
            hallway_spots = filter(lambda a: a not in [(1, 3), (1, 5), (1, 7), (1, 9)], product((1,), range(1, 12)))
            for spot in hallway_spots:
                if possible(s, pos, spot):
                    yield spot


def solve(s):
    pieces = filter(lambda a: a[1] in ['A', 'B', 'C', 'D'], s.items())
    # recursion break: are we done?
    if all(x[0][1] == room_map[x[1]] for x in pieces):
        return 0  # valid state
    best_solution = inf
    for p in pieces:
        for m in moves(s, p[0]):
            s[m] = p[1]
            s[p[0]] = '.'
            gs = map_to_str(s)
            print(gs)
            if gs in states_map:
                curr_cost = states_map[gs]
            else:
                curr_cost = solve(s) + cost_map[p[1]] * (abs(p[0][0] - m[0]) + abs(p[0][1] - m[1]))
                states_map[gs] = curr_cost
            if curr_cost < best_solution:
                best_solution = curr_cost
            s[p[0]] = p[1]
            s[m] = '.'
    return best_solution


print(solve(state))

#print(len(states_map))


