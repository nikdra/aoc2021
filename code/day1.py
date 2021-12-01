# aoc 2021 day 1 part 1

# read input, cast to int
depths = open('../input/day1.txt').read().splitlines()
depths = [int(x) for x in depths]

# print outcome
print(sum([y > x for x, y in zip(depths[:-1], depths[1:])]))

# part 2
# intermediate list of sum of three depths
three_sum = [x + y + z for x, y, z in zip(depths[:-2], depths[1:-1], depths[2:])]

# print outcome
print(sum([y > x for x, y in zip(three_sum[:-1], three_sum[1:])]))
