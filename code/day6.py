# aoc 2021 day 6 part 1
# read input
fish = list(map(int, open('../input/day6.txt').read().split(',')))


def simulate(fishes, steps):
    # create list of fish
    # index is the days to reproduction (0, 1, 2, 3, 4, 5, 6, 7, 8): 9 values
    # value is number of fish
    reproduction_groups = [0] * 9
    for f in fishes:
        reproduction_groups[f] += 1
    for i in range(steps):
        # only one of the age groups will reproduce offspring
        # it will be offspring that is 8 days away from reproducing
        # this is basically a ringbuffer operation
        reproduction_groups[(i + 7) % 9] += reproduction_groups[i % 9]
    return sum(reproduction_groups)


# simulate population
print(simulate(fish, 80))

# part 2
# simulate population
print(simulate(fish, 256))
