# aoc 2021 day 12 part 1
# read input
inp = [[a for a in line.split('-')] for line in open('../input/day12.txt').read().splitlines()]


# basically DFS
def explore(caves, path):
    if path[-1] == 'end':  # recursion break, we found the exit
        return 1  # return 1. this is a valid path
    if path[-1].islower() and path[-1] in path[:-1]:  # recursion break, invalid choice
        return 0  # return 0, this has lead nowhere (valid)
    # get all possible next caves (big or small)
    possible_routes = (a[0] if a[1] == path[-1] else a[1] for a in filter(lambda a: path[-1] in a, caves))
    # return number of possible paths
    return sum(explore(caves, path + [conn]) for conn in possible_routes)


print(explore(inp, ['start']))

# part 2


# variation of the above function
def explore_further(caves, path):
    # get all possible next caves (big or small)
    possible_routes = (a[0] if a[1] == path[-1] else a[1] for a in filter(lambda a: path[-1] in a, caves))
    if path[-1] == 'end':  # recursion break, we found the exit
        return 1  # return 1. this is a valid path
    if path[-1].islower() and path[-1] in path[:-1]:  # this is a small cave we've visited before
        if path[-1] == 'start':  # can't visit start cave twice, break recursion
            return 0  # return 0, this has lead nowhere (valid)
        # use our "double small cave" bonus. use explore function from above from here on in
        return sum(explore(caves, path + [conn]) for conn in possible_routes)
    # return number of possible paths
    return sum(explore_further(caves, path + [conn]) for conn in possible_routes)


print(explore_further(inp, ['start']))
