# aoc 2021 day 23 part 1
from math import inf
from itertools import product, chain


def map_to_str(s):
    grid = [[' ' for _ in range(13)] for _ in range(max(a[0] for a in s)+1)]
    for (i, j), v in s.items():
        grid[i][j] = v
    grid_str = '\n'.join(''.join(line) for line in grid)
    return grid_str


def possible(s, start, end):
    if start[0] == 1 or end[0] == 1:  # room-hallway or hallway-room
        miny = min(start[1], end[1])
        maxy = max(start[1], end[1])
        hallway_move = product((1,), range(miny, maxy+1))
        minx = min(start[0], end[0])
        maxx = max(start[0], end[0])
        room_num = start[1] if start[0] != 1 else end[1]
        room_move = product(range(minx, maxx+1), (room_num,))
        ch = chain(hallway_move, room_move)
    else:  # room-room
        miny = min(start[1], end[1])
        maxy = max(start[1], end[1])
        hallway_move = product((1,), range(miny, maxy + 1))
        room1_move = product(range(1, start[0] + 1), (start[1],))
        room2_move = product(range(1, end[0] + 1), (end[1],))
        ch = chain(hallway_move, room1_move, room2_move)
    if any(s[p] != '.' for p in ch if p != start):
        return False  # can't jump over other piece
    else:  # free lane
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
        # if the room is incomplete or in the wrong room
        if any(s[(k, pos[1])] not in [piece, '.'] for k in range(2, 4)) or room_map[piece] != pos[1]:
            hallway_spots = filter(lambda a: a not in [(1, 3), (1, 5), (1, 7), (1, 9)], product((1,), range(1, 12)))
            for spot in hallway_spots:
                if possible(s, pos, spot):
                    yield spot
            # move directly into room
            if s[3, room_map[piece]] == '.':  # room not occupied
                if possible(s, pos, (3, room_map[piece])):
                    yield 3, room_map[piece]
            elif s[3, room_map[piece]] == piece and s[2, room_map[piece]] == '.':  # room occupied with correct amoeba
                if possible(s, pos, (2, room_map[piece])):
                    yield 2, room_map[piece]


def solve(s, moves_fun=moves):
    pieces = list(filter(lambda a: a[1] in ['A', 'B', 'C', 'D'], s.items()))
    # memoization
    gs = map_to_str(s)
    if gs in states_map:  # we know the solution from here
        return states_map[gs]
    # recursion break: are we done?
    if all(x[0][1] == room_map[x[1]] for x in pieces):
        return 0  # valid state
    best_solution = inf
    for p in pieces:
        for m in moves_fun(s, p[0]):
            s[m] = p[1]
            s[p[0]] = '.'
            curr_cost = solve(s, moves_fun) + cost(p[1], p[0], m)
            if curr_cost < best_solution:
                best_solution = curr_cost
            s[p[0]] = p[1]
            s[m] = '.'
    states_map[gs] = best_solution
    return best_solution


def cost(piece, start, end):
    if start[0] == 1 or end[0] == 1:  # move from/to hallway: manhattan distance
        return cost_map[piece] * (abs(start[0] - end[0]) + abs(start[1] - end[1]))
    else:  # room to room
        return cost_map[piece] * ((start[0] - 1) + abs(start[1] - end[1]) + 1 + (end[0] - 1))


def moves_4(s, pos):
    piece = s[pos]
    assert piece in ['A', 'B', 'C', 'D']
    if pos[0] == 1:  # standing in hallway, must move into room
        if s[5, room_map[piece]] == '.':  # room not occupied
            if possible(s, pos, (5, room_map[piece])):
                yield 5, room_map[piece]
        elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == '.':  # room occupied with correct amoeba
            if possible(s, pos, (4, room_map[piece])):
                yield 4, room_map[piece]
        elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == piece and s[3, room_map[piece]] == '.':  # room occupied with correct amoeba
            if possible(s, pos, (3, room_map[piece])):
                yield 3, room_map[piece]
        elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == piece and s[3, room_map[piece]] == piece and s[2, room_map[piece]] == '.':  # room occupied with correct amoeba
            if possible(s, pos, (2, room_map[piece])):
                yield 2, room_map[piece]
    else:  # standing in a room
        # if the room is incomplete or we're in the wrong room
        if any(s[(k, pos[1])] not in [piece, '.'] for k in range(2, 6)) or room_map[piece] != pos[1]:
            hallway_spots = filter(lambda a: a not in [(1, 3), (1, 5), (1, 7), (1, 9)], product((1,), range(1, 12)))
            for spot in hallway_spots:
                if possible(s, pos, spot):
                    yield spot
            # move directly into room
            if s[5, room_map[piece]] == '.':  # room not occupied
                if possible(s, pos, (5, room_map[piece])):
                    yield 5, room_map[piece]
            elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == '.':  # room occupied with correct amoeba
                if possible(s, pos, (4, room_map[piece])):
                    yield 4, room_map[piece]
            elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == piece and s[3, room_map[piece]] == '.':  # room occupied with correct amoeba
                if possible(s, pos, (3, room_map[piece])):
                    yield 3, room_map[piece]
            elif s[5, room_map[piece]] == piece and s[4, room_map[piece]] == piece and s[3, room_map[piece]] == piece and s[2, room_map[piece]] == '.':  # room occupied with correct amoeba
                if possible(s, pos, (2, room_map[piece])):
                    yield 2, room_map[piece]


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

# part 1
state = [[x for x in line] for line in open("../input/day23.txt").read().splitlines()]
state = [[(i, j, state[i][j]) for j in range(len(state[i]))] for i in range(len(state))]

state = {
    (i, j): v for (i, j, v) in [item for sublist in state for item in sublist]
}

print(solve(state))

# part 2
state = [[x for x in line] for line in open("../input/day23_2.txt").read().splitlines()]
state = [[(i, j, state[i][j]) for j in range(len(state[i]))] for i in range(len(state))]

state = {
    (i, j): v for (i, j, v) in [item for sublist in state for item in sublist]
}

states_map = dict()

print(solve(state, moves_4))
