from functools import reduce

area = []


def basin_size(i, j: int) -> int:

    if i < 0 or j < 0 or i >= len(area) or j >= len(area[i]):
        return 0

    if area[i][j] is None:
        return 0

    if area[i][j] == 9:
        return 0

    area[i][j] = None
    return (
        1
        + basin_size(i - 1, j)
        + basin_size(i + 1, j)
        + basin_size(i, j - 1)
        + basin_size(i, j + 1)
    )


for line in open("input_9.txt"):
    stripped_line = line.strip()
    area.append([int(c) for c in stripped_line])

basins = {}
for i in range(len(area)):
    for j in range(len(area[i])):
        if area[i][j] is None:
            continue
        if i > 0:
            if area[i - 1][j] is not None and area[i - 1][j] <= area[i][j]:
                continue
        if i < len(area) - 1:
            if area[i + 1][j] is not None and area[i + 1][j] <= area[i][j]:
                continue
        if j > 0:
            if area[i][j - 1] is not None and area[i][j - 1] <= area[i][j]:
                continue
        if j < len(area[i]) - 1:
            if area[i][j + 1] is not None and area[i][j + 1] <= area[i][j]:
                continue

        size = basin_size(i, j)
        if size > 0:
            basins[(i, j)] = size

print(basins)

sorted_sizes = sorted(list(basins.values()))
print(sorted_sizes)

product = reduce(lambda p, c: p * c, sorted_sizes[-3:])
print(product)
