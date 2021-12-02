# aoc 2021 day 2 part 1

# read input
commands = list(map(lambda x: (x[0], int(x[1])),
                    [x.split() for x in open('../input/day2.txt').read().splitlines()]))

movements = {
    'up': lambda posx, posy, k: (posx, posy-k),
    'down': lambda posx, posy, k: (posx, posy+k),
    'forward': lambda posx, posy, k: (posx + k, posy)
}

# move in direction
pos = (0, 0)
for i in range(len(commands)):
    pos = movements[commands[i][0]](*pos, commands[i][1])

# print outcome
print(pos[0]*pos[1])

# part 2
movements = {
    'up': lambda posx, posy, aim, k: (posx, posy, aim-k),
    'down': lambda posx, posy, aim, k: (posx, posy, aim+k),
    'forward': lambda posx, posy, aim, k: (posx + k, posy + aim*k, aim)
}

# move in direction
pos = (0, 0, 0)
for i in range(len(commands)):
    pos = movements[commands[i][0]](*pos, commands[i][1])

# print outcome
print(pos[0]*pos[1])
