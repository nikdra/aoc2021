# aoc 2021 day 21 part 1
from functools import lru_cache

# read input - starting position of the players
positions = [int(x.split(' ')[-1]) for x in open('../input/day21.txt').read().splitlines()]


# play the game until one player has 1000 points
def play(pos1, pos2, s1=0, s2=0, turn=0):
    if s1 >= 1000 or s2 >= 1000:
        return s1 if s1 < 1000 else s2, turn*3  # return loser score and die rolls
    # get roll sum
    rolls = sum((turn*3 + k) % 100 + 1 for k in range(0, 3))
    if turn % 2 == 0:  # player one
        position = (pos1 + rolls) % 10 if (pos1 + rolls) % 10 != 0 else 10
        # continue playing
        return play(position, pos2, s1 + position, s2, turn + 1)
    else:
        position = (pos2 + rolls) % 10 if (pos2 + rolls) % 10 != 0 else 10
        # continue playing
        return play(pos1, position, s1, s2 + position, turn + 1)


loser, die_rolls = play(positions[0], positions[1])
# loser score times the number of times the die has been cast
print(loser * die_rolls)


# part 2
# play with a dirac die
# we can make it a bit simpler by only considering the _sums_ that can occur in one round
# so instead of 3*3*3 possible die rolls, it's only 7 possible roll sums
# returns number of wins for each player from a game state/universe
@lru_cache(maxsize=None)
def play_quantum(pos1, pos2, s1=0, s2=0, turn=0):
    if s1 >= 21:  # first player won
        return [1, 0]
    if s2 >= 21:  # second player won
        return [0, 1]
    # play one round
    sums = {6: 7, 5: 6, 7: 6, 4: 3, 8: 3, 3: 1, 9: 1}  # map of sums: universes they occur in
    wins = [0, 0]  # number of times players win in this universe's universes
    for rolls, universes in sums.items():  # for each possible roll sum
        if turn == 0:  # player one plays
            position = (pos1 + rolls) % 10 if (pos1 + rolls) % 10 != 0 else 10
            # wins is number of universes with that roll sum in this universe * number of wins then
            universe_wins = play_quantum(position, pos2, s1 + position, s2, (turn + 1) % 2)
        else:  # player two plays
            position = (pos2 + rolls) % 10 if (pos2 + rolls) % 10 != 0 else 10
            # wins is number of universes with that roll sum in this universe * number of wins then
            universe_wins = play_quantum(pos1, position, s1, s2 + position, (turn + 1) % 2)
        wins[0] += universes * universe_wins[0]
        wins[1] += universes * universe_wins[1]
    return wins  # return number of wins for each player


# player wins with dirac die
dubs = play_quantum(positions[0], positions[1], turn=0)

# how often did the player win that won more often
print(max(dubs))
