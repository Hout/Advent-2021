from typing import Tuple, List
from functools import reduce


def parse(bitstream: str, pointer: int, length: int) -> Tuple[str, int]:
    new_pointer = pointer + length
    fragment = bitstream[pointer:new_pointer]
    return fragment, new_pointer


def parse_int(bitstream: str, pointer: int, length: int) -> Tuple[int, int]:
    fragment, pointer = parse(bitstream=bitstream, pointer=pointer, length=length)
    return int(fragment, 2), pointer


def get_packet(bit_str: str, pointer: int) -> Tuple[List, int]:

    # analyse packet
    version, pointer = parse_int(bit_str, pointer, 3)
    type_id, pointer = parse_int(bit_str, pointer, 3)
    if type_id == 4:
        # literal
        number_str = ""
        while True:
            block, pointer = parse(bit_str, pointer, 5)
            number_str += block[1:]
            if block[0] == "0":
                break
        return [int(number_str, 2)], pointer

    # operator
    packets = []
    length_type_id, pointer = parse_int(bit_str, pointer, 1)
    if length_type_id == 0:
        # number of bits
        length, pointer = parse_int(bit_str, pointer, 15)
        end = pointer + length
        while pointer < end:
            packet, pointer = get_packet(bit_str, pointer)
            packets.extend(packet)
    else:
        # number of sub packets
        length, pointer = parse_int(bit_str, pointer, 11)
        for i in range(length):
            packet, pointer = get_packet(bit_str, pointer)
            packets.extend(packet)

    if type_id == 0:
        result = sum(packets)
    elif type_id == 1:
        result = reduce(lambda p, c: p * c, packets, 1)
    elif type_id == 2:
        result = min(packets)
    elif type_id == 3:
        result = max(packets)
    elif type_id == 5:
        result = 1 if packets[0] > packets[1] else 0
    elif type_id == 6:
        result = 1 if packets[0] < packets[1] else 0
    elif type_id == 7:
        result = 1 if packets[0] == packets[1] else 0
    else:
        assert False

    return [result], pointer


lines = open("input_16.txt").read().splitlines()

for line in lines:
    hex_list = [int(c, 16) for c in line]
    bit_str = "".join(str(f"{h:04b}") for h in hex_list)
    print(get_packet(bit_str, 0))
