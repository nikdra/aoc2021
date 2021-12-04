# aoc 2021 day 4 part 1
import numpy as np

# read input
inp = open("../input/day4.txt").read().splitlines()

# get the numbers to draw from
nums = np.array([int(x) for x in inp[0].split(',')])

# get boards as 5x5 arrays
boards = np.array([[list(map(int, filter(lambda x: x != '', row.split(' ')))) for row in inp[i:i + 5]]
                   for i in range(2, len(inp), 6)])


# play bingo by calculating "win number" and score for each board
def calculate_win_number_score(board, marks, num_list, i=0):
    # play
    num = num_list[i]
    marks[board == num] = True
    # calculate win condition (any row or any column has 5 marked spots)
    if any(np.sum(marks, axis=0) == 5) or any(np.sum(marks, axis=1) == 5):
        # we're done: win number = number of turns, score = sum of unmarked * last number called
        return [i, int(np.sum(board[marks==False]) * num)]
    return calculate_win_number_score(board, marks, num_list, i+1)


# calculate win number for each board
win_numbers_scores = np.array([calculate_win_number_score(board, np.zeros((5, 5)), nums) for board in boards])
# get minimum index of win number with score
print(win_numbers_scores[np.argmin(win_numbers_scores[:, 0]), 1])

# part 2
# get maximum index of win number with score
print(win_numbers_scores[np.argmax(win_numbers_scores[:, 0]), 1])
