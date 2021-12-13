# aoc 2021 day 13 part 1

# read input
inp = open('../input/day13.txt').read().splitlines()

# store (x,y) points in a set so that double points after folding are eliminated
points = set()
points.update(tuple(map(int, line.split(','))) for line in inp if 'fold' not in line and line != '')

# create instructions (axis, line) generator
instructions = map(lambda a: (a[0], int(a[1])), [line[11:].split('=') for line in inp if 'fold' in line])


# fold the paper according to the instruction
def fold_paper(pts, inst):
    if inst[0] == 'y':  # fold over y
        pts_to_fold = list(filter(lambda a: a[1] > inst[1], pts))  # get points to fold (below fold line)
        pts -= set(pts_to_fold)  # remove those points from the list
        # new point: x-coord stays the same, new y coord is 2*fold line-old y
        pts.update(map(lambda a: (a[0], 2*inst[1]-a[1]), pts_to_fold))  # add folded points to set of points
    else:  # fold over x
        pts_to_fold = list(filter(lambda a: a[0] > inst[1], pts))  # get points to fold (right of fold line)
        pts -= set(pts_to_fold)  # remove those points from the list
        pts.update(map(lambda a: (2*inst[1] - a[0], a[1]), pts_to_fold))  # add folded points to set of points


# fold once
fold_paper(points, next(instructions))
# part 1 answer - number of points
print(len(points))

# part 2
# continue folding
for instruction in instructions:
    fold_paper(points, instruction)

# get max coordinate for final grid
xmax = max(map(lambda a: a[0], points))
ymax = max(map(lambda a: a[1], points))

# print grid string from points
print('\n'.join([''.join(['██' if (i, j) in points else '░░' for i in range(xmax+1)]) for j in range(ymax+1)]))
