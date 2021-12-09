# aoc 2021 day 9 part 1
from collections import deque, Counter
from functools import reduce
from operator import mul

# read input
heatmap = [[int(num) for num in line] for line in open('../input/day9.txt').read().splitlines()]


def neighbors(x, y, arr):  # get neighbors of x, y in an array (list of lists)
    if x > 0:
        yield x-1, y
    if y > 0:
        yield x, y-1
    if x < len(arr) - 1:
        yield x+1, y
    if y < len(arr[x]) - 1:
        yield x, y+1


# get low points coordinates
# low point is a point that is strictly lower than all its neighbors
low_points = reduce(lambda a, b: a+b,
                    [[(x, y) for y in range(len(heatmap[x]))
                      if heatmap[x][y] < min(heatmap[x][y] for x, y in neighbors(x, y, heatmap))]
                     for x in range(len(heatmap))])

# print result
# sum of (value+1 of low point) for each low point
print(sum(heatmap[x][y] + 1 for x, y in low_points))


# part 2
def get_basin_sizes(seed_points, arr):  # basically region growing with multiple seeds
    visited = set()  # this set denotes all points we have visited with the basin id
    neighbor_stack = deque()  # the stack of neighbors we have to visit
    # region growing seeds, mark each seed with a different id
    neighbor_stack.extend(((x, y),  i) for i, (x, y) in enumerate(seed_points))
    # we make use of the fact that one point can only be part of one basin, so one set is enough
    while len(neighbor_stack) > 0:  # while we have neighbors to visit
        (x, y), i = neighbor_stack.pop()  # get the neighbor
        if (x, y, i) not in visited:  # not part of basin yet
            visited.add((x, y, i))  # add to basin
            nbs = neighbors(x, y, arr)  # get neighbors
            # filter out the suitable neighbors - must be higher than their predecessor and lower than nine
            nbs = filter(lambda a: arr[a[0]][a[1]] > arr[x][y] and arr[a[0]][a[1]] != 9, nbs)
            # add them to the neighbor stack with id
            neighbor_stack.extend(((a, b), i) for a, b in nbs)

    # get the number of times each id appears in the basin mask
    basin_sizes = Counter(i for _, _, i in visited)
    return reduce(mul, sorted(basin_sizes.values(), reverse=True)[:3])


# get result
print(get_basin_sizes(low_points, heatmap))
