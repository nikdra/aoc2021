# aoc 2021 day 22 part 1
import re

# read input
r = r'(on|off)\sx=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'
inp = [[re.match(r, x).groups()[0]] + list(map(int, re.match(r, x).groups()[1:]))
       for x in open('../input/day22.txt').read().splitlines()]


class Cuboid:
    # class wrapper for a cuboid
    def __init__(self, x1, x2, y1, y2, z1, z2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.z1 = z1
        self.z2 = z2
        self.off = []  # list of cuboids that should be off

    def coords(self):  # the coordinates of this cuboid
        return self.x1, self.x2, self.y1, self.y2, self.z1, self.z2

    def overlap(self, x1, x2, y1, y2, z1, z2):  # determine the overlap of two cuboids. only works if they overlap
        return Cuboid(max(self.x1, x1), min(self.x2, x2),
                      max(self.y1, y1), min(self.y2, y2),
                      max(self.z1, z1), min(self.z2, z2))

    def subtract(self, other):  # subtract a cuboid from this cuboid
        if self.overlaps(*other.coords()):  # if it overlaps
            o = self.overlap(*other.coords())  # compute overlap
            for of in self.off:  # for each cuboid that is in this cuboid
                of.subtract(o)  # subtract it
            self.off.append(o)  # and add this cuboid to the list of cuboids that should be subtracted

    def overlaps(self, x1, x2, y1, y2, z1, z2):  # true if cuboid overlaps with coordinates, false otherwise
        return ((self.x1 <= x1 <= self.x2 or x1 <= self.x1 <= x2) and
                (self.y1 <= y1 <= self.y2 or y1 <= self.y1 <= y2) and
                (self.z1 <= z1 <= self.z2 or z1 <= self.z1 <= z2))

    def num_cubes(self):  # number of cubes in this cuboid: volume - volume of cuboids to subtract
        return (self.x2 - self.x1 + 1) * (self.y2 - self.y1 + 1) * (self.z2 - self.z1 + 1) - sum(o.num_cubes() for o
                                                                                                 in self.off)


cube_list = set()  # all our cuboids

for cub in inp:
    # only consider cubes in input with coordinates in -50..50
    if all(abs(x) <= 50 for x in cub[1:]):
        cuboid = Cuboid(*cub[1:])
        for c in cube_list:
            c.subtract(cuboid)  # subtract this cuboid from all other cuboids
        if cub[0] == 'on':  # is it on or off?
            cube_list.add(cuboid)

print(sum(c.num_cubes() for c in cube_list))  # print total number of cubes

# part 2
# do the same thing, but with all cubes
cube_list = set()

for cub in inp:
    cuboid = Cuboid(*cub[1:])
    for c in cube_list:
        c.subtract(cuboid)
    if cub[0] == 'on':
        cube_list.add(cuboid)

print(sum(c.num_cubes() for c in cube_list))
