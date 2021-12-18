# aoc 2021 day 18 part 1
import ast
from functools import reduce

# convert string representation of list to "real" list
inp = list(map(ast.literal_eval, open('../input/day18.txt').read().splitlines()))


# function to reduce a snail number
def reduce_node(node):
    exploded, new_node, _, _ = explode(*node)  # try to force an explosion in the snail number
    if not exploded:  # no explosion
        splitted, new_node = split(*node)  # try to force a split in the snail number
    if exploded or splitted:  # yes explosion
        return reduce_node(new_node)  # gotta reduce again
    # if we're here we did neither explode nor split. therefore, we're done.
    return node


# function to try and force a split in the snail number
def split(left, right):
    if type(left) == int:
        if left >= 10:  # split left?
            new_left = [left // 2, left - left // 2]
            return True, [new_left, right]  # this can be split
    else:
        splitted, new_left = split(*left)  # split on the left subtree?
        if splitted:
            return splitted, [new_left, right]
    if type(right) == int:
        if right >= 10:  # split right?
            new_right = [right // 2, right - right//2]
            return True, [left, new_right]
    else:
        splitted, new_right = split(*right)  # split on the right subtree?
        if splitted:
            return splitted, [left, new_right]
    return False, [left, right]  # no split in this (sub-) tree


# function to try and force an explosion in the snail number
def explode(left, right, depth=0):
    if depth == 4:  # explosion condition
        return True, 0, left, right   # EXPLOOOOOOSION (insert megumin meme here)
    # explode on left subtree?
    if type(left) != int:
        to_explode, left_tree, l_value, r_value = explode(*left, depth=depth + 1)
        if to_explode:
            # return modified tree bottom up
            if r_value > 0:  # if we came from the left, we must propagate the right value to the left
                return True, [left_tree, add(right, r_value, "left")], l_value, -1
            else:  # nothing
                return True, [left_tree, right], l_value, r_value
    # explode on right subtree?
    if type(right) != int:
        to_explode, right_tree, l_value, r_value = explode(*right, depth=depth + 1)
        if to_explode:
            if l_value > 0:  # if we came from the right, we must propagate the left value to the right
                return True, [add(left, l_value, "right"), right_tree], -1, r_value
            else:  # nothing
                return True, [left, right_tree], l_value, r_value
    return False, [left, right], -1, -1  # nothing to explode here


# function to add a value to a node, if possible
def add(node, value, direction):
    if type(node) == int:
        return node + value
    if direction == "left":
        return [add(node[0], value, "left"), node[1]]
    else:
        return [node[0], add(node[1], value, "right")]
    # can happen that we end up here, but that's alright. less to do for us.


def magnitude(node):
    # magnitude of a node = 3*left magnitude + 2*right magnitude. If leaf, then the value
    if type(node) == int:
        return node
    return 3*magnitude(node[0]) + 2*magnitude(node[1])


# magnitude of sum of snail numbers, starting from the top
print(magnitude(reduce(lambda a, b: reduce_node([a, b]), inp)))

# part 2
# maximum magnitude from the sum of any two snail numbers
print(max(magnitude(reduce_node([a, b])) for a in inp for b in inp if a != b))

