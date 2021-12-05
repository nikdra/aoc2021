# aoc day 3 part 1
import numpy as np

# read input
report = np.array([[c for c in x] for x in open('../input/day3.txt').read().splitlines()], int)

# transform 0 bits to -1 => if sum is positive, then 1 is more common, else 0
report[report == 0] = -1

# calculate gamma as a bit array
gamma = np.sum(report, axis=0).clip(min=0, max=1)
# calculate epsilon: 1-gamma (bit array)
epsilon = 1 - gamma

# print result, convert to base 10
print(int(''.join(str(x) for x in gamma), base=2) * int(''.join(str(x) for x in epsilon), base=2))


# part 2
def get_life_support(entries, i, oxygen=True):
    if len(entries) == 1:  # recursion break, we're done
        oxygen = entries[0].clip(min=0, max=1)
        return int(''.join(str(x) for x in oxygen), base=2)  # transform the entry to base 2 and then base 10
    # get most/least common bit
    if oxygen:
        bit = 1 if np.sum(entries[:, i]) >= 0 else -1
    else:
        bit = -1 if np.sum(entries[:, i]) >= 0 else 1
    return get_life_support(entries[entries[:, i] == bit], i+1, oxygen)  # keep searching


# print outcome
print(get_life_support(report, 0) * get_life_support(report, 0, False))
