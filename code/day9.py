# aoc 2021 day 9 part 1
import numpy as np
from collections import deque
from functools import reduce

# read input
heatmap = np.array([[int(num) for num in line] for line in open('../input/day9.txt').read().splitlines()])


def neighbors(xdim, ydim, x, y):
    xs = [x-1, x+1, x, x]
    ys = [y, y, y-1, y+1]
    # because of how numpy indexing works:
    # return tuple of two n-tuples. first n-tuple is x-coord, second n-tuple is y-coord i.e.,
    # ((0, 2, 1, 1), (1, 1, 0, 2)) = (0,1), (2,1), (1,0), (1,2) // neighbors of (1,1)
    return tuple(zip(*((x, y) for x, y in zip(xs, ys) if (0 <= x < xdim) and (0 <= y < ydim))))


# get low points coordinates
# low point is a point that is strictly lower than all its neighbors
low_points = tuple(zip(*((x, y) for y in range(len(heatmap[0])) for x in range(len(heatmap)) if heatmap[(x, y)] <
                         min(heatmap[neighbors(len(heatmap), len(heatmap[0]), x, y)]))))

# print result
# sum of (value of low point+1) for each low point
print(sum(heatmap[low_points] + 1))


# part 2
def get_basin_sizes(seed_points, arr):  # basically region growing with multiple seeds
    basin_mask = np.zeros_like(arr)  # this array denotes all points we have visited
    neighbor_stack = deque()  # the stack of neighbors we have to visit
    # region growing seeds, mark each seed with a different id
    neighbor_stack.extend((a, arr[a], i+1) for i, a in enumerate(zip(*seed_points)))
    # for convenience: array dimensions for neighbor search
    xdim = len(arr)
    ydim = len(arr[0])
    # we make use of the fact that one point can only be part of one basin, so one mask is enough
    while len(neighbor_stack) > 0:  # while we have neighbors to visit
        position, value, i = neighbor_stack.pop()  # get the neighbor
        if basin_mask[position] == 0:  # not part of basin yet
            basin_mask[position] = i  # add to basin
            nbs = neighbors(xdim, ydim, *position)  # get neighbors
            # filter out the suitable neighbors - must be higher than their predecessor and lower than nine
            nbs = filter(lambda a: arr[a] > value and arr[a] != 9, zip(*nbs))
            neighbor_stack.extend([(a, arr[a], i) for a in nbs])  # add them to the neighbor stack with value and id

    # get the number of times each id (including 0 for non-visited points) appears in the basin mask
    _, basin_sizes = np.unique(basin_mask, return_counts=True)
    # return the product of the three largest basins
    return reduce(lambda a, b: a*b, sorted(basin_sizes[1:], reverse=True)[:3])


# get result
print(get_basin_sizes(low_points, heatmap))
# find all basin sizes and sort descending
# basins = sorted((get_basin_size(*pos, heatmap) for pos in zip(*low_points)), reverse=True)
# multiply sizes of the three largest basins for the result
# print(reduce(lambda a, b: a*b, basins[:3]))
