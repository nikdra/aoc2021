# aoc 2021 day 17 part 1
import re
from math import sqrt

# read input
inp = open("../input/day17.txt").readline()

# get the target area values
m = re.match(r"target area: x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)", inp)

target_area = list(map(int, (m.group(i) for i in range(1, 5))))

# show highest possible height of projectile
# max y velo for highest point => must be that one that drops exactly at the bottom of the target area
# => -ymin-1, because -ymin would drop the projectile out of the target because of 0 momentum at the top
# highest position is then the sum of 1..-ymin-1
print(-target_area[2]*(-target_area[2]-1)//2)


# part 2
def step(x, y, v):  # make a step in the projectile function
    return (x+v[0], y+v[1]), (max(0, v[0]-1), v[1]-1)


def hits_target(v, area):  # function that asserts whether an init velocity hits a target area
    pos = 0, 0
    while True:
        pos, v = step(*pos, v)  # update position, velocity
        if pos[0] > area[1] or (pos[0] < area[0] and v[0] == 0) or pos[1] < area[2]:  # miss
            return False
        if area[0] <= pos[0] <= area[1] and area[2] <= pos[1] <= area[3]:  # hit target
            return True


# max x velo is the one that shoots directly into the target area far edge
# min x velo is the one that shoots at the near edge after a sufficient number of steps n^2+n-xmin=0
# min and max y velo are those that can reasonably hit the target: (positive and negative) of absolute value of ymin
# brute force everything inbetween
count = sum(hits_target((x_v, y_v), target_area)
            for x_v in range(int(-1/2 + sqrt(1/4 + target_area[0])), target_area[1]+1)
            for y_v in range(target_area[2]-1, -target_area[2]+1))
# show distinct number of velocities that hit the target
print(count)
