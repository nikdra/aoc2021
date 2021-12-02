# aoc 2021 day 1 part 1

# read input, cast to int
depths = list(map(int, open('../input/day1.txt').read().splitlines()))

# print outcome
print(sum([y > x for x, y in zip(depths[:-1], depths[1:])]))

# part 2
# intermediate list of sum of three depths
# a + b + c < b + c + d iff a < d
# print outcome
print(sum([y > x for x, y in zip(depths[:-3], depths[3:])]))
