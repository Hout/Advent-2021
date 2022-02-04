from typing import Tuple


def get_pair(line, key="") -> Tuple:
    a = None
    b = None
    pos = 1
    if line[pos] == "[":
        # pair
        a, a_pos = get_pair(line[pos:])
        pos += a_pos
    else:
        # int
        a = int(line[pos])
        pos += 1
    assert line[pos] == ","
    pos += 1
    if line[pos] == "[":
        # pair
        b, b_pos = get_pair(line[pos:])
        pos += b_pos
    else:
        # int
        b = int(line[pos])
        pos += 1
    assert line[pos] == "]"
    pos += 1
    return (a, b), pos


def explode_shape(pair: Tuple) -> Tuple:
    pass


def reduce_shape(pair: Tuple) -> bool:
    return type(pair) == "Tuple[Tuple[int, int], Tuple[int, int]]"


def reduce(pair: Tuple, top_pair=None, level=0) -> Tuple:
    if top_pair is None and level == 0:
        top_pair = pair



    reduce(p, top_pair=top_pair, level=level+1)
    if level==4:


    for e in pair:
        while len(address) < level + 1:
            address.append[0]
        address[level] = i




def add(pair1: Tuple, pair2: Tuple) -> Tuple:
    return reduce((pair1, pair2))


for line in open("input_18t.txt"):
    stripped_line = line.strip()
    p, pos = get_pair(stripped_line)
    assert pos == len(stripped_line)
