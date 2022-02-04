import re
from collections import namedtuple
from typing import Tuple


Area = namedtuple("Area", "x1 x2 y1 y2")
Point = namedtuple("Point", "x y")


def hit(area: Area, p: Point) -> bool:
    return p.x >= area.x1 and p.x <= area.x2 and p.y >= area.y1 and p.y <= area.y2


def movement(p: Point, hv: int, vv: int) -> Tuple[Point, int, int]:
    x = p.x
    y = p.y

    x += hv
    if hv > 0:
        hv -= 1
    elif hv < 0:
        hv += 1

    y += vv
    vv -= 1
    return (Point(x, y), hv, vv)


lines = open("input_17.txt").read().splitlines()
for line in lines:
    m = re.match(
        r"target area: x=([+-]?\d+)..([+-]?\d+), y=([+-]?\d+)..([+-]?\d+)", line
    )
    area = Area(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)))
    print(f"Area={area}")

    height = area.y2 - area.y1 + 1
    width = area.x2 - area.x1 + 1

    assert area.x1 > 0 and area.x2 > area.x1
    assert area.y2 > area.y1 and (area.y1 > 0 or area.y2 < 0)

    hits = set()

    # firing up, the bullet always passes y=0 and the previous or next is vv or vv+1 respectively
    # maximum vertical velocity is top of area when area is above y=0 or
    # bottom of area - 1 when below y=0
    vv_max = max(abs(area.y1), abs(area.y1))

    for start_vv in range(area.y1, vv_max):
        for start_hv in range(
            min(area.x1, area.x2) if area.x1 < 0 else 1,
            max(area.x1, area.x2) + 1 if area.x1 > 0 else 0,
        ):
            vv = start_vv
            hv = start_hv

            # shoot!
            p = Point(0, 0)
            positions = []

            # going up first
            while vv > 0 or p.y >= area.y1:
                if hit(area, p):
                    hits.add((start_hv, start_vv, len(positions)))
                    break
                p, hv, vv = movement(p, hv, vv)
                positions.append(p)

    for hit in sorted(list(hits)):
        print(hit)
    print(len(hits))
