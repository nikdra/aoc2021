# aoc 2021 day 8 part 1
import numpy as np

# read input
inp = open('../input/day8.txt').read().splitlines()
patterns = [line.split(' | ')[0].split() for line in inp]
output_values = [line.split(' | ')[1].split() for line in inp]

# unique numbers 1, 4, 7, 8 use 2, 4, 3, 7 segments respectively
print(sum(sum(len(y) in [2, 3, 4, 7] for y in x) for x in output_values))


# part 2
def get_output(pattern, output):
    # first, calculate map from the pattern
    # sort all elements in a pattern alphabetically
    pattern = ["".join(sorted(p)) for p in pattern]

    # unique patterns
    one = next(filter(lambda a: len(a) == 2, pattern))
    four = next(filter(lambda a: len(a) == 4, pattern))
    seven = next(filter(lambda a: len(a) == 3, pattern))
    eight = "abcdefg"
    # the only character with 6 segments that contains four is nine
    nine = next(filter(lambda a: all(c in a for c in four) and len(a) == 6, pattern))
    # the only character with 6 segments that contains one is zero
    zero = next(filter(lambda a: a != nine and all(c in a for c in one) and len(a) == 6, pattern))
    # the only other character with 6 segments is six
    six = next(filter(lambda a: a not in (zero, nine) and len(a) == 6, pattern))
    # the only character with 5 segments that contains one is three
    three = next(filter(lambda a: all(c in a for c in one) and len(a) == 5, pattern))
    # the only character with 5 segments that is contained in nine and not three is five
    five = next(filter(lambda a: a != three and all(c in nine for c in a) and len(a) == 5,  pattern))
    # the only remaining character with five segments is two
    two = next(filter(lambda a: a not in (three, five) and len(a) == 5, pattern))
    # create a map
    segments_num = {x: str(i) for i, x in enumerate([zero, one, two, three, four, five, six, seven, eight, nine])}

    # sort all elements in the output alphabetically
    # get the numeric string for each segment string in the output
    # cast to int and return
    return int(''.join([segments_num[num] for num in [''.join(sorted(p)) for p in output]]))


# get sum of outputs
print(sum(get_output(pat, ov) for pat, ov in zip(patterns, output_values)))
