# aoc 2021 day 5 part 1
import numpy as np

# read input
inp = open("../input/day5.txt").read().splitlines()

# get lines as nx4 array of x1, y1, x2, y2
lines = np.array([list(map(int, line.split(' -> ')[0].split(','))) + list(map(int, line.split(' -> ')[1].split(',')))
                  for line in inp])

# compute dx (first element of row), dy (second element of row) in ds
ds = np.array([lines[:, 2] - lines[:, 0], lines[:, 3] - lines[:, 1]]).transpose()
# number of steps we have to make on the line: biggest absolute difference between dx and dy
steps = np.amax(np.abs(ds), axis=1)
# direction we have to go in for x and y
signs = np.sign(ds)

# get points of all lines
points = np.array([[[pts[0] + si[0] * k, pts[1] + si[1] * k] for k in range(st+1)] for pts, st, si
                   in zip(lines[:, :2], steps, signs)], dtype=object)
# horizontal or vertical line condition for selection of points
hv_condition = np.logical_or(lines[:, 0] == lines[:, 2], lines[:, 1] == lines[:, 3])
# get list of these points in a flat list
hv_points = np.array([item for sublist in points[hv_condition] for item in sublist])
# get the number of unique points and their number of occurrence
_, counts = np.unique(hv_points, return_counts=True, axis=0)
# get number of elements that occur more than once
print(np.sum(counts > 1))

# part 2
# get list of all points in a flat list
points = np.array([item for sublist in points for item in sublist])
# get the number of unique points and their number of occurrence
_, counts = np.unique(points, return_counts=True, axis=0)
# get number of elements that occur more than once
print(np.sum(counts > 1))
