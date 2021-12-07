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

# bonus
# dynamic programming-ish solution. cache up to 256 calls
c = [-1] * 256


# function to calculate how many fish are in a colony after `a` days, starting with one fish reproducing on day 0
def fun(a):
    if a <= 0:
        return 1  # less than 1 day? 1
    if c[a] != -1:  # we know this one!
        return c[a]  # return cached result
    val1 = fun(a-7)  # future version of itself
    val2 = fun(a-9)  # and one offspring
    c[a] = val1 + val2  # add up the offspring they produce and cache
    return c[a]  # return result


# part 1
print(sum(fun(80-fi) for fi in fish))
# part 2
print(sum(fun(256-fi) for fi in fish))
