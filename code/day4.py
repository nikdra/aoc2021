# aoc 2021 day 4 part 1
# import numpy as np

# read input
inp = open("../input/day4.txt").read().splitlines()

# get the numbers to draw from
nums = [int(x) for x in inp[0].split(',')]

# get boards as 5x5 arrays
boards = [[list(map(int, filter(lambda x: x != '', row.split(' ')))) for row in inp[i:i + 5]]
          for i in range(2, len(inp), 6)]


# calculate the number of turns needed and the score for a play board, marker board and number list
# by default start with an empty marker board and the first number in the list
def calculate_turns_score(board, num_list, marks=None, i=0):
    if marks is None:
        marks = [[0 for _ in range(len(board[i]))] for i in range(len(board))]
    # play: set marker where the board has the drawn number
    # marks[board == num_list[i]] = 1
    marks = [[1 if board[k][j] == num_list[i] else marks[k][j] for j in range(len(board[k]))]
             for k in range(len(board))]
    # calculate win condition (any row or any column has 5 marked spots)
    colsum = [sum(marks[i][col] for i in range(len(marks))) for col in range(len(marks[0]))]
    rowsum = [sum(row) for row in marks]
    if any([r == 5 for r in rowsum]) or any([c == 5 for c in colsum]):
        # we're done: win number = number of turns, score = sum of unmarked * last number called
        # return [i, int(np.sum(board[marks == 0]) * num_list[i])]  # exit recursion
        return [i, sum(sum(board[k][j] for j in range(len(board[k])) if marks[k][j] == 0)
                       for k in range(len(board))) * num_list[i]]
    return calculate_turns_score(board, num_list, marks, i+1)  # continue playing with next number


# calculate turns needed and score for each board and sort by number of turns needed
win_numbers_scores = sorted(map(lambda x: calculate_turns_score(x, nums), boards), key=lambda x: x[0])
# get score of board that needs the least turns
print(win_numbers_scores[0][1])

# part 2
# get score of board that needs the most turns
print(win_numbers_scores[-1][1])
