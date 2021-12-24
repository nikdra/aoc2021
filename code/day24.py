# aoc 2021 day 24 part 1
# this can only really be solved by looking at the input and figuring out what it does.
# i mean, it can be brute forced. there are, however, 9^14 possibilities (which is a number with 14 digits)
# read about it here: https://github.com/mrphlip/aoc/blob/master/2021/24.md
# basically, the digits are pushed onto a stack and the stack is only empty if the top element of the stack satisfies
# a condition on the first number

# suppose the 14-digit number is ABCDEFGHIJLKMN
# the equations that have to be satisfied in our input are:
# A + 4 = L
# B - 5 = K
# C + 3 = J
# D - 7 = E
#     F = G
# H + 5 = I
# M - 1 = N

# the maximum number that satisfies the equations is: 59692994994998
# the minimum number that satisfies the equations is: 16181111641521

max_input = "59692994994998"
min_input = "16181111641521"

# for easy lookup - store instruction functions in a dict
instruction_dict = {
    "add": lambda a, b: a + b,
    "mul": lambda a, b: a*b,
    "div": lambda a, b: a // b,
    "mod": lambda a, b: a % b,
    "eql": lambda a, b: 1 if a == b else 0
}


# execute the instructions with a given input number
def execute(instructions, input_number, var_dict=None, instruction_pointer=0, input_pointer=0):
    if var_dict is None:  # init the variables with 0
        var_dict = {k: 0 for k in 'wxyz'}
    if instruction_pointer == len(instructions):  # last instruction read, return true if value in z is zero, else false
        return var_dict['z'] == 0
    inst = instructions[instruction_pointer]  # read instruction
    if inst[0] == 'inp':  # read next input number
        var_dict[inst[1]] = int(input_number[input_pointer])
        input_pointer += 1
    else:  # ..or do calculation
        first_argument = var_dict[inst[1]]
        second_argument = var_dict[inst[2]] if inst[2] in ['w', 'x', 'y', 'z'] else int(inst[2])
        if inst[0] == 'div' and second_argument == 0:
            return False  # invalid arguments to div, return false to avoid magic smoke
        if inst[0] == 'mod' and (first_argument < 0 or second_argument <= 0):
            return False  # invalid arguments to mod, return false to avoid magic smoke
        # execute calculation, store in first variable
        var_dict[inst[1]] = instruction_dict[inst[0]](first_argument, second_argument)

    # execute next instruction
    return execute(instructions, input_number, var_dict, instruction_pointer+1, input_pointer)


# read input (cast integers to int)
inp = [list(map(lambda a: int(a) if a.lstrip('-').isnumeric() else a, x.split()))
       for x in open('../input/day24.txt').read().splitlines()]

# show that the numbers are accepted
# part 1
print(execute(inp, max_input))
# part 2
print(execute(inp, min_input))
