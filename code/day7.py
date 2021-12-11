# aoc 2021 day 7 part 1

# read input
positions = list(map(int, open('../input/day7.txt').readline().split(',')))

# minimum E(|X-c| - |X|) = median
# get sum of required fuel to get to position = sum of absolute deviations from the median
median = sorted(positions)[len(positions) // 2]
print(sum(abs(median-pos) for pos in positions))

# part 2
# the average is "good enough" to produce the correct input
# however, we have to try both integers closest to the average
# sum of natural numbers = n*(n+1)/2
# in our case: abs(pos-average) * (abs(pos-average) + 1) / 2
# numpy can do this in one go for all pos in positions
ave = sum(positions) / len(positions)
lower_bound = int(ave)
upper_bound = lower_bound + 1

fl = sum(a*b for a, b in zip((abs(lower_bound-pos) for pos in positions),
                             (abs(lower_bound-pos) + 1 for pos in positions))) // 2
cl = sum(a*b for a, b in zip((abs(upper_bound-pos) for pos in positions),
                             (abs(upper_bound-pos) + 1 for pos in positions))) // 2

# minimum of 97164405, 97164301
print(min(fl, cl))
