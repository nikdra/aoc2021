# aoc 2021 day 25 part 1
from itertools import chain

# read input
inp = [[x for x in line] for line in open('../input/day25.txt').read().splitlines()]

# know when we have to loop around
bottom_edge = len(inp)

right_edge = len(inp[0])

# convert input to dict of positions
inp = [[(i, j, inp[i][j]) for j in range(len(inp[i])) if inp[i][j] != '.'] for i in range(len(inp))]

init_state = {
    (i, j): v for (i, j, v) in [item for sublist in inp for item in sublist]
}


# function to determine the next position for a south-facing cucumber
def next_south(x, y):
    return (x+1) % bottom_edge, y


# function to determine the next position for an east-facing cucumber
def next_east(x, y):
    return x, (y+1) % right_edge


steps = 0
old_state = init_state.copy()
while True:
    moved = False  # have we moved this step?
    steps += 1  # increase number of steps taken
    new_state = dict()  # store the next state

    # for each cucumber in the east-facing herd: move it, if possible
    first_herd = filter(lambda a: old_state[a] == '>', old_state.keys())
    for pos in first_herd:
        next_pos = next_east(*pos)
        if next_pos not in old_state:
            moved = True
            new_state[next_pos] = '>'
        else:
            new_state[pos] = '>'

    # now we have to combine the new positions of the east-facing herd with the current position of the other herd
    intermediate_positions = set(p for p in chain(new_state.keys(),
                                                  filter(lambda a: old_state[a] == 'v', old_state.keys())))

    # same thing as above, but for the south-facing herd
    second_herd = filter(lambda a: old_state[a] == 'v', old_state.keys())
    for pos in second_herd:
        next_pos = next_south(*pos)
        if next_pos not in intermediate_positions:
            moved = True
            new_state[next_pos] = 'v'
        else:
            new_state[pos] = 'v'

    # carry over this new state
    old_state = new_state.copy()

    # did any cucumber move?
    if not moved:
        break


# print number of steps it took for the cucumbers to stop moving
print(steps)
