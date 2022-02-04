from functools import reduce


def fuel(distance: int) -> int:
    return distance * (distance + 1) // 2


crab_lst = [int(f) for f in open("input_7.txt").readline().strip().split(",")]

d = {}
min_value = None
min_i = None
for i in range(min(crab_lst), max(crab_lst) + 1):
    d[i] = reduce(lambda p, c: p + fuel(abs(c - i)), crab_lst, 0)
    if min_value is None or min_value > d[i]:
        min_value = d[i]
        min_index = i

print(d)
print(min_index, min_value)
