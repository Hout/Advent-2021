from typing import Tuple


def parse(bitstream: str, position: int, length: int) -> Tuple[str, str]:
    new_position = position + length
    fragment = bitstream[position:new_position]
    return fragment, new_position


def parse_int(bitstream: str, position: int, length: int) -> Tuple[str, int]:
    fragment, pointer = parse(bitstream=bitstream, position=position, length=length)
    return int(fragment, 2), pointer


total_version = 0


def get_packet(bit_str: str, pointer: int) -> int:
    global total_version

    # analyse packet
    version, pointer = parse_int(bit_str, pointer, 3)
    total_version += version
    type_id, pointer = parse_int(bit_str, pointer, 3)
    if type_id == 4:
        # literal
        number_str = ""
        while True:
            block, pointer = parse(bit_str, pointer, 5)
            number_str += block[1:]
            if block[0] == "0":
                break
        number = int(number_str, 2)
    else:
        # operator
        length_type_id, pointer = parse_int(bit_str, pointer, 1)
        if length_type_id == 0:
            # number of bits
            length, pointer = parse_int(bit_str, pointer, 15)
            end = pointer + length
            while pointer < end:
                pointer = get_packet(bit_str, pointer)
        else:
            # number of sub packets
            length, pointer = parse_int(bit_str, pointer, 11)
            for i in range(length):
                pointer = get_packet(bit_str, pointer)

    return pointer


lines = open("input_16.txt").read().splitlines()

for line in lines:
    hex_list = [int(c, 16) for c in line]
    bit_str = "".join(str(f"{h:04b}") for h in hex_list)
    get_packet(bit_str, 0)

print(total_version)
