# aoc 2021 day 5 part 1

# read input
inp = open("../input/day5.txt").read().splitlines()

# get lines as nx4 array of x1, y1, x2, y2
lines = [list(map(int, line.split(' -> ')[0].split(','))) + list(map(int, line.split(' -> ')[1].split(',')))
         for line in inp]

points = {}
hv_points = {}

for x1, y1, x2, y2 in lines:
    if x1 == x2 or y1 == y2:
        if y1 == y2:  # horizontal line
            xs = range(x1, x2+1 if x2 > x1 else x2-1, 1 if x2-x1 > 0 else -1)
            ys = [y1] * (abs(x1-x2) + 1)
        else:  # vertical line
            xs = [x1] * (abs(y1-y2) + 1)
            ys = range(y1, y2+1 if y2 > y1 else y2 - 1, 1 if y2-y1 > 0 else -1)
        for pt in zip(xs, ys):
            points[pt] = points.get(pt, 0) + 1
            hv_points[pt] = hv_points.get(pt, 0) + 1
    else:
        xs = range(x1, x2 + 1 if x2 > x1 else x2 - 1, 1 if x2 - x1 > 0 else -1)
        ys = range(y1, y2 + 1 if y2 > y1 else y2 - 1, 1 if y2 - y1 > 0 else -1)
        for pt in zip(xs, ys):
            points[pt] = points.get(pt, 0) + 1

# part 1
print(sum(x > 1 for x in hv_points.values()))
# part 2
print(sum(x > 1 for x in points.values()))
