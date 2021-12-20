# aoc 2021 day 20 part 1

def neighborhood(x, y, dic, rnd, inst):
    # must account for the fact that the image is infinite, and therefore, the values of the pixels might change in
    # the infinite space. Does not work if the first and last char of the algorithm are '#'.
    # (infinite lit pixels after 1 round anyway)
    if inst[0] == '.':
        alternate_value = '.'
    else:
        alternate_value = '#' if (rnd % 2) == 1 else '.'

    return (((x+i, y+j), '1' if dic.get((x+i, y+j), alternate_value) == '#' else '0')
            for i in range(-1, 2) for j in range(-1, 2))


# read input
inp = open('../input/day20.txt').read().splitlines()
# first line is the algorithm
algo = inp[0]

# get image as dict with pos: value pairs
dt = [[(i, j, v) for j, v in enumerate(line)] for i, line in enumerate(inp[2:])]

img = {(i, j): v for (i, j, v) in [item for sublist in dt for item in sublist]}


def enhance(pixels, enh, rounds):
    # enhance an image for k rounds
    old_values = pixels  # do not change the original image
    for r in range(rounds):
        new_values = dict()  # remember updated values
        # account for corners
        x_bounds = (min(old_values.keys(), key=lambda a: a[0])[0] - 2,
                    max(old_values.keys(), key=lambda a: a[0])[0] + 3)
        y_bounds = (min(old_values.keys(), key=lambda a: a[1])[1] - 2,
                    max(old_values.keys(), key=lambda a: a[1])[1] + 3)

        # put the pixels we have to iterate over in a stack
        pixel_stack = ((i, j) for i in range(x_bounds[0], x_bounds[1])
                       for j in range(y_bounds[0], y_bounds[1]))
        for pixel in pixel_stack:
            # get neighbor values as 0, 1 by row, column
            ns = list(neighborhood(*pixel, old_values, r, enh))
            # get the index we have to query in the algorithm string
            enh_value = enh[int(''.join(n[1] for n in ns), 2)]
            # store updated value
            new_values[pixel] = enh_value
        # carry over the updated values
        old_values = new_values.copy()

    # return enhanced image
    return old_values


# enhance twice
pt1 = enhance(img, algo, 2)
# how many pixels are lit?
print(sum(x == '#' for x in pt1.values()))

# part 2
# enhance 50 times
pt2 = enhance(img, algo, 50)
# how many pixels are lit?
print(sum(x == '#' for x in pt2.values()))
