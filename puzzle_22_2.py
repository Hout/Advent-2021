import re


def volume(c) -> int:
    _, (x1, x2), (y1, y2), (z1, z2) = c
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1) * (abs(z1 - z2) + 1)


def intersection(c1, c2):
    intersecting = []
    for coords1, coords2 in zip(c1[1:], c2[1:]):
        if coords1[0] > coords2[1] or coords2[0] > coords1[1]:
            return None
        intersecting.append((max(coords1[0], coords2[0]) - min(coords1[1], coords2[1])))
    return tuple(intersecting)


cuboids = []
for line in open("input_22_1t2.txt").read().split("\n"):
    status, x1, x2, y1, y2, z1, z2 = re.match(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", line
    ).groups()
    cuboids.append(
        (status == "on", (int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2)))
    )


def total_volume(cuboids):
    result = 0
    for i1, c1 in enumerate(cuboids):
        if c1[0]:
            result += volume(c1)
        for i2 in range(i1):
            c2 = cuboids[i2]
            int = intersection(c1, c2)
            if not int:
                continue
            result -= volume(intersection)


print(total_volume)
