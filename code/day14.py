# aoc 2021 day 14 part 1
from collections import Counter

# read input
inp = open('../input/day14.txt').read().splitlines()

# first line is the polymer template
template = inp[0]

# everything from the third line is substitution rules. store them as a dict.
rules = {line.split(' -> ')[0]: line.split(' -> ')[1] for line in inp[2:]}


# a function that counts the number of occurrences of a character in a polymer template that has been extended for
# k pair insertion steps
def steps(poly, r, k):
    # get the pairs in the polymer as a dict with the number of times they occur
    pairs = Counter([poly[i:i+2] for i in range(len(poly)-1)])
    # count the number of times a character occurs in the template
    counts = Counter(poly)
    for _ in range(k):  # for k steps
        new_pairs = dict()  # create a new dict for the pairs created by this step
        for p in pairs:  # for each distinct pair
            # the insertion creates two pairs by inserting a character in the middle
            # the new pairs occur as often as the pair occurs in the current polymer
            new_pairs[p[0] + r[p]] = new_pairs.get(p[0] + r[p], 0) + pairs[p]
            new_pairs[r[p] + p[1]] = new_pairs.get(r[p] + p[1], 0) + pairs[p]
            # increase the count of the newly inserted characters
            counts[r[p]] = counts.get(r[p], 0) + pairs[p]
        pairs = new_pairs  # update the pairs in the polymer
    # return quantity of the most common element and subtract the quantity of the least common element
    return max(counts.values()) - min(counts.values())


# result after 10 steps
print(steps(template, rules, 10))

# part 2
# do the same thing for 40 steps
print(steps(template, rules, 40))
