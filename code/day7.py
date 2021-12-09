# aoc 2021 day 7 part 1
import numpy as np

# read input
positions = np.array(list(map(int, open('../input/day7.txt').readline().split(','))))

# minimum E(|X-c| - |X|) = median
# get sum of required fuel to get to position = sum of absolute deviations from the median
print(sum(np.abs(positions-int(np.median(positions)))))

# part 2
# the average is "good enough" to produce the correct input
# however, we have to try both integers closest to the average
# sum of natural numbers = n*(n+1)/2
# in our case: abs(pos-average) * (abs(pos-average) + 1) / 2
# numpy can do this in one go for all pos in positions
ave = np.average(positions)
fl = int(sum(abs(positions - np.floor(ave))*(abs(positions - np.floor(ave))+1)/2))
cl = int(sum(abs(positions - np.ceil(ave))*(abs(positions - np.ceil(ave))+1)/2))

# minimum of 97164405, 97164301
print(min(fl, cl))


# we can also brute force it
def calculate_fuel(_positions, _k):
    return int(sum(abs(_positions - _k) * (abs(_positions - _k) + 1)/2))


# possible final position must be a value that occurs in the list of current positions
print(min([calculate_fuel(positions, k) for k in range(min(positions), max(positions)+1)]))
