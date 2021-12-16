# aoc 2021 day 16 part 1
import abc
from functools import reduce

# read input
inp = open('../input/day16.txt').readline()


def hex_to_binary(hex_string):
    # first two characters are 0b - remove them; add leading zeros as necessary
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


# convert to binary
bits = hex_to_binary(inp)


class Node(metaclass=abc.ABCMeta):
    # abstract class for a node in the operator tree
    def __init__(self, version):
        self.version = version

    @abc.abstractmethod
    def get_version_sum(self):  # get the sum of versions in the tree with this node as root
        pass

    @abc.abstractmethod
    def eval(self):  # get the value of the tree with this node as root
        pass


class Literal(Node):
    # class to represent a literal (value)
    def __init__(self, version, value):
        super().__init__(version)
        self.value = value

    def get_version_sum(self):  # this is a leaf, therefore return this version number
        return self.version

    def eval(self):  # this is a literal, return the value stored
        return self.value


class Operator(Node):
    # class to represent a non-leaf node
    def __init__(self, version, type_id, sub_packets):
        super().__init__(version)
        self.type_id = type_id
        self.sub_packets = sub_packets

    def get_version_sum(self):  # version sum is this version + sum of versions in the subtrees
        return self.version + sum(p.get_version_sum() for p in self.sub_packets)

    @staticmethod
    def mul(v):  # function to multiply all values in an array
        return reduce(lambda a, b: a * b, v)

    @staticmethod
    def gt(v):  # function to assert whether the first value is greater than the second
        return 1 if next(v) > next(v) else 0

    @staticmethod
    def lt(v):  # function to assert whether the first value is less than the second
        return 1 if next(v) < next(v) else 0

    @staticmethod
    def eq(v):  # function to assert if two values are equal
        return 1 if next(v) == next(v) else 0

    def eval(self):  # evaluate according to the operator type
        op = {  # operator dict. key is the type id, value is the function it represents
            0: sum,
            1: Operator.mul,
            2: min,
            3: max,
            5: Operator.gt,
            6: Operator.lt,
            7: Operator.eq
        }
        return op[self.type_id](p.eval() for p in self.sub_packets)


def parse(transmission, pos=0) -> (Node, int):  # parse the bit string into an operator tree
    version = int(transmission[pos:pos + 3], 2)  # version number
    type_id = int(transmission[pos + 3:pos + 6], 2)  # literal or operator?
    pos += 6  # this is the offset from the start
    if type_id == 4:
        num = ''
        while True:  # read the number
            num = num + transmission[pos + 1:pos + 5]
            pos += 5  # move position pointer
            if transmission[pos - 5] == '0':  # this was the last part of the number
                return Literal(version, int(num, 2)), pos  # return literal node and position
    else:
        length_type_id = transmission[pos]  # how should we process the sub packets in this operator
        packets = []  # hold the sub packets
        pos += 1  # move the position pointer
        if length_type_id == '0':
            # length of sub packets is given
            sub_packets_length = int(transmission[pos:pos + 15], 2)  # read the sub packets length
            pos += 15  # move position pointer
            content_start = pos  # remember at which position we started reading
            while sub_packets_length != pos-content_start:  # while we haven't read all the sub-packets
                packet, pos = parse(transmission, pos)
                packets.append(packet)  # add sub packet to sub packet list
        else:  # length type id 1
            # number of sub packets is given
            num_sub_packets = int(transmission[pos:pos + 11], 2)  # read the number of sub packets
            pos += 11  # move position pointer
            for i in range(num_sub_packets):  # while we haven't read all the sub-packets
                packet, pos = parse(transmission, pos)
                packets.append(packet)  # add sub packet to sub packet list

        # return operator node and packet length
        return Operator(version, type_id, packets), pos


# parse bit string into operator tree
root, _ = parse(bits)
# print sum of versions of the nodes
print(root.get_version_sum())

# part 2
# evaluate the operator tree
print(root.eval())
