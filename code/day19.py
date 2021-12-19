# aoc 2021 day 19 part 1
import numpy as np
from itertools import product
from collections import deque

# read input
inp = ''.join(open('../input/day19.txt').readlines())

# get the beacon positions for each scanner in a matrix/numpy array
scanners = [np.array([list(map(int, p.split(','))) for p in l.split('\n')[1:]]) for l in inp.split('\n\n')]

# generate rotation matrices
# possible columns/rows must contain 2 zeros and either +1 or -1
possible_cols = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]

# for all distinct 90 degree rotation matrices:
# row sum of absolute values = 1
# col sum of absolute values = 1
# determinant = 1 (could be -1 for mirrors)
matrices = list(filter(lambda a: np.all(np.sum(abs(a), 0) == 1) and np.all(np.sum(abs(a), 1) == 1) and
                                 np.linalg.det(a) == 1,
                       (np.array(m) for m in product(possible_cols, possible_cols, possible_cols))))

# to the meat of the piece: finding the number of beacons and the position of the scanners in the 3D space
# we assume the orientation of scanner zero as the "true" orientation with scanner zero's position at (0,0,0)

# we store the scanner positions we know in a map
scanner_positions = {
    0: np.array([0, 0, 0])
}

# get the unique distances of the beacons to each other for each scanner
scanner_beacons_distances = {
    k: [x for x in np.unique(np.linalg.norm(a[:, None, :] - a[None, :, :], axis=-1).flatten()) if x > 0]
    for k, a in enumerate(scanners)
}

# record the number of times the pairwise distances of beacons are the same for each pair of scanners
common_distances = {
    (i, k): len([x for x in scanner_beacons_distances[k] if x in scanner_beacons_distances[i]]) for i, k in
    product(scanner_beacons_distances, scanner_beacons_distances)
}

# in order not to check any pairs of scanners more often than we have to
# we can determine the set of pairs for which it is possible that there is an intersection of at least 12 beacons
# that is those pairs of scanners which have more than 66 pairwise distances that are equal
# 66 is the number of edges in a fully connected (undirected) graph
# we remove duplicates (i, j) and (j, i) and put the pairs with scanner 0 at the front
pairs = deque(sorted(set(
    tuple(sorted(x)) for x in common_distances if common_distances[x] >= 66 and x[0] != x[1]
), key=lambda a: a[0], reverse=True))  # put zero at the start

print(len(pairs), " distinct pairs to check")

while len(pairs) > 0:  # while there is something to check
    (sj, sk) = pairs.pop()
    print("checking ", sj, sk)
    if sj in scanner_positions and sk in scanner_positions:
        print("solved pair: ", (sj, sk))
        continue  # this is a solved pair
    if sj not in scanner_positions and sk not in scanner_positions:
        print("not yet solvable: ", (sj, sk))
        pairs.appendleft((sj, sk))  # put on end of queue
        continue
    if sj not in scanner_positions:  # sj = known scanner, sk = unknown scanner
        temp = sk
        sk = sj
        sj = temp
    found = False  # variable to break out of rotation - translation brute force
    for rot in matrices:  # for each of the 24 possible rotations
        rotated_beacons = scanners[sk].dot(rot)  # rotate the coordinates of the new beacon
        for v in map(lambda a: a[0] - a[1], product(scanners[sj], rotated_beacons)):
            # for each possible translation (n^2 possibilities)
            rotated_translated_beacons = rotated_beacons + v
            # check if the rotated and translated points have 12 points in common
            old_beacons = set(map(tuple, scanners[sj]))
            new_beacons = set(map(tuple, rotated_translated_beacons))
            inter = old_beacons.intersection(new_beacons)
            if len(inter) >= 12:  # we found a match for the new beacon
                # record beacon and scanner positions in our canonical coord. system
                scanners[sk] = rotated_translated_beacons
                scanner_positions[sk] = v
                print(sk, " solved")
                found = True  # break out, no unnecessary calculations
            if found:
                break  # break out, no unnecessary calculations
        if found:
            break  # break out, no unnecessary calculations
    if not found:
        print("No match found for", (sj, sk))
        pairs.appendleft((sj, sk))

# now that we have all the beacons in our normalized coordinate system, we can count how many unique ones there are
beacons = set()
for s in scanners:
    beacons.update(map(tuple, s))  # because sets do not like lists

# part 1
# how many unique beacons are there?
print(len(beacons))

# part 2
# maximum manhattan distance between two beacons
print(max(sum(abs(a-b)) for a, b in product(scanner_positions.values(), scanner_positions.values())))
