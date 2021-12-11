# aoc 2021 day 11 part 1


def neighbors(row, col, array):  # get neighbors of row, col in an array (list of lists)
    if row > 0:
        yield row-1, col
    if col > 0:
        yield row, col-1
    if row < len(array) - 1:
        yield row+1, col
    if col < len(array[row]) - 1:
        yield row, col+1
    # include diagonals
    if row > 0 and col > 0:
        yield row-1, col-1
    if row < len(array) - 1 and col < len(array[row]) - 1:
        yield row+1, col+1
    if row < len(array) - 1 and col > 0:
        yield row+1, col-1
    if row > 0 and col < len(array[row]) - 1:
        yield row-1, col+1


# read input
arr = [[int(x) for x in line] for line in open('../input/day11.txt').read().splitlines()]

# part 1 and 2 in one
# simulate
steps = 0
flashes = 0
all_flashed = False
while steps < 100 or not all_flashed:  # while i still haven't found what i'm looking for
    steps += 1
    # first, the energy level of each octopus increases by one
    arr = [[p + 1 for p in line] for line in arr]
    flashed = [[False for _ in line] for line in arr]  # octopus can only flash once
    # then, any octopus with an energy level greater than 9 flashes
    while any([any([p > 9 for p in line]) for line in arr]):  # while an octopus can flash
        # loop over array entries
        for x in range(len(arr)):
            for y in range(len(arr[x])):
                if arr[x][y] > 9 and not flashed[x][y]:  # octopus with high energy level and no flash this round
                    flashed[x][y] = True  # it flashed
                    arr[x][y] = 0  # set energy to zero
                    for x1, y1 in neighbors(x, y, arr):  # increase energy level for each octopus in neighborhood
                        if not flashed[x1][y1]:  # only an unflashed octopus can increase its energy level
                            arr[x1][y1] += 1
    flashes += sum((sum(line) for line in flashed))  # add number of flashes this step to the total
    if steps == 100:  # part 1
        print("Number of Flashes after 100 steps: ", flashes)
    # part 2 - did they all flash?
    if sum((sum(line) for line in flashed)) == sum(sum(1 for _ in line) for line in arr) and not all_flashed:
        all_flashed = True
        print("First step when all flashed: ", steps)
