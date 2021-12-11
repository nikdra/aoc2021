# aoc day 3 part 1

# read input
report = [[int(c) for c in x] for x in open('../input/day3.txt').read().splitlines()]

# transform 0 bits to -1 => if sum is positive, then 1 is more common, else 0
report = [[x if x > 0 else -1 for x in y] for y in report]

# calculate gamma as a bit array
gamma = list(map(lambda a: 1 if a > 1 else 0 if a < 0 else a,
                 [sum(report[i][col] for i in range(len(report))) for col in range(len(report[0]))]))
# calculate epsilon: 1-gamma (bit array)
epsilon = [1 - g for g in gamma]

# print result, convert to base 10
print(int(''.join(str(x) for x in gamma), base=2) * int(''.join(str(x) for x in epsilon), base=2))


# part 2
def get_life_support(entries, i, oxygen=True):
    if len(entries) == 1:  # recursion break, we're done
        # transform -1, 1 to 0, 1
        oxygen = map(lambda a: 1 if a > 1 else 0 if a < 0 else a, entries[0])
        return int(''.join(str(x) for x in oxygen), base=2)  # transform the entry to base 2 and then base 10
    # get most/least common bit for column
    if oxygen:
        bit = 1 if sum(entries[row][i] for row in range(len(entries))) >= 0 else -1
    else:
        bit = -1 if sum(entries[row][i] for row in range(len(entries))) >= 0 else 1
    # keep searching with entries that have the most/least common bit at i
    return get_life_support(list(filter(lambda a: a[i] == bit, entries)), i+1, oxygen)


# print outcome
print(get_life_support(report, 0) * get_life_support(report, 0, False))
