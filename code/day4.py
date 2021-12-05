# aoc 2021 day 4 part 1
import numpy as np

# read input
inp = open("../input/day4.txt").read().splitlines()

# get the numbers to draw from
nums = np.array([int(x) for x in inp[0].split(',')])

# get boards as 5x5 arrays
boards = np.array([[list(map(int, filter(lambda x: x != '', row.split(' ')))) for row in inp[i:i + 5]]
                   for i in range(2, len(inp), 6)])


# calculate the number of turns needed and the score for a play board, marker board and number list
# by default start with an empty marker board and the first number in the list
def calculate_turns_score(board, num_list, marks=None, i=0):
    if marks is None:
        marks = np.zeros((5, 5))
    # play: set marker where the board has the drawn number
    marks[board == num_list[i]] = 1
    # calculate win condition (any row or any column has 5 marked spots)
    if any(np.sum(marks, axis=0) == 5) or any(np.sum(marks, axis=1) == 5):
        # we're done: win number = number of turns, score = sum of unmarked * last number called
        return [i, int(np.sum(board[marks == 0]) * num_list[i])]  # exit recursion
    return calculate_turns_score(board, num_list, marks, i+1)  # continue playing with next number


# calculate turns needed and score for each board and sort by number of turns needed
win_numbers_scores = sorted(map(lambda x: calculate_turns_score(x, nums), boards), key=lambda x: x[0])
# get score of board that needs the least turns
print(win_numbers_scores[0][1])

# part 2
# get score of board that needs the most turns
print(win_numbers_scores[-1][1])
