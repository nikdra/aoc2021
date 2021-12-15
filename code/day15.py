# aoc 2021 day 15 part 1
import math
from queue import PriorityQueue

# read input
inp = [[int(x) for x in line] for line in open('../input/day15.txt').read().splitlines()]


def neighbors(x, y, arr):  # get 4-neighbors of (x, y) in an array arr
    if x > 0:
        yield x - 1, y
    if y > 0:
        yield x, y - 1
    if x < len(arr) - 1:
        yield x + 1, y
    if y < len(arr[x]) - 1:
        yield x, y + 1


def lowest_risk_path(cave):  # a* algorithm from wikipedia
    # our goal is the bottom right of the cave
    goal = (len(cave) - 1, len(cave[-1]) - 1)

    # set of nodes that may have to be re-expanded
    openSet = PriorityQueue(maxsize=len(cave)*len(cave[-1]))
    # initially, only the start node is known (cost 0)
    openSet.put((0, (0, 0)))

    # the currently known cost of the lowest risk path from the start to the node
    gScore = {(i, j): math.inf for i in range(len(cave)) for j in range(len(cave[0]))}
    gScore[(0, 0)] = 0

    # a heuristic to estimate the remaining cost from a node to the goal
    def h(row, col):  # admissible heuristic: manhattan distance to goal never overestimates-optimum guaranteed
        return abs(row - len(cave) + 1) + abs(col - len(cave[-1]) + 1)

    while not openSet.empty():
        _, current = openSet.get()  # get node with lowest cost
        if current == goal:  # we found our goal
            return gScore[goal]  # return the cost

        for n in neighbors(*current, cave):
            tentative_gScore = gScore[current] + cave[n[0]][n[1]]  # calculate the cost from start to each neighbor
            if tentative_gScore < gScore[n]:  # new low: record it
                gScore[n] = tentative_gScore
                fScore = tentative_gScore + h(*n)  # update estimated cost from neighbor to goal
                if n not in openSet.queue:  # add to the set of nodes that may have to be re-expanded
                    openSet.put((fScore, n))

    # we failed (never happens though)
    return None


# show lowest possible risk for a path from top left to bottom right
print(lowest_risk_path(inp))


def expanded_value(a, value):  # function to expand a cave given the "distance" to the initial cave
    return 9 if (a+value) % 9 == 0 else (a+value) % 9


# part 2
# expand cave according to the rules
inp_new = []
for i in range(5):
    new_row = None
    for j in range(5):
        list2 = [[expanded_value(i+j, inp[l][k]) for k in range(len(inp[l]))] for l in range(len(inp))]
        if new_row is None:
            new_row = list2
        else:
            new_row = list(map(lambda a, b: a+b, new_row, list2))
    inp_new.extend(new_row)


# show lowest possible risk for a path from top left to bottom right
print(lowest_risk_path(inp_new))
