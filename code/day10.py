# aoc 2021 day 10 part 1
from collections import deque
from functools import reduce

# read input
lines = open('../input/day10.txt').read().splitlines()

complementary_bracket = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


# check syntax of a line
# if it's corrupted, return a flag that it's corrupted together with the points for the corrupted character
# otherwise, return the points for the completion of the line
def syntax_check(line):
    stack = deque()
    for c in line:  # for each character in the line
        if c in ['(', '[', '{', '<']:  # opening bracket
            stack.append(c)  # add on top of the stack
        else:
            op = stack.pop()  # pop last opening bracket from the stack
            if c != complementary_bracket[op]:
                return True, points[c]  # return the value of the corrupted character
    # we found an incomplete line
    # return the points for the completion
    # get the completion string (complement of reverse of stack elements), transform to points,
    # then apply the scoring rule
    return False, reduce(lambda a, b: a * 5 + b, (completion_points[complementary_bracket[c]]
                                                  for c in reversed(stack)), 0)


# for each line:
# if it's corrupted, set flag to true and get the character points
# if it's incomplete, set flag to false and get the completion points
checked_lines = [syntax_check(line) for line in lines]

# sum up the points of corrupted characters
print(sum(c for _, c in filter(lambda a: a[0], checked_lines)))

# part 2

# sort the scores of completed characters
scores = sorted(c for _, c in filter(lambda a: not a[0], checked_lines))

# print the middle score (we have a guarantee that the number of incomplete lines is odd)
print(scores[len(scores)//2])
