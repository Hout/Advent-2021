import re
from collections import defaultdict, Counter
from typing import Tuple
import numpy as np


Coords = Tuple[int, int, int]


def sin(degrees: int) -> int:
    return {0: 0, 90: 1, 180: 0, 270: -1, 360: 0}[degrees]


def cos(degrees: int) -> int:
    return sin(degrees + 90)


def orientations(coords: Coords) -> Coords:
    vector = np.array(coords)

    directions = range(0, 360, 90)
    for degrees_x in directions:
        matrix_x = np.array(
            [
                [1, 0, 0],
                [0, cos(degrees_x), -sin(degrees_x)],
                [0, sin(degrees_x), cos(degrees_x)],
            ]
        )
        vector = np.matmul(vector, matrix_x)

        for degrees_y in directions:
            matrix_y = np.array(
                [
                    [cos(degrees_y), 0, sin(degrees_y)],
                    [0, 1, 0],
                    [-sin(degrees_y), 0, cos(degrees_y)],
                ]
            )
            vector = np.matmul(vector, matrix_y)

            for degrees_z in directions:
                matrix_z = np.array(
                    [
                        [cos(degrees_z), -sin(degrees_z), 0],
                        [sin(degrees_z), cos(degrees_z), 0],
                        [0, 0, 1],
                    ]
                )
                vector = np.matmul(vector, matrix_z)

                yield vector.tolist()


beacons = defaultdict(list)
for line in open("input_19t.txt"):
    line_s = line.strip()
    if line_s == "":
        continue
    m = re.match(r"--- scanner (\d+) ---", line)
    if m is not None:
        scanner = int(m.group(1))
        continue
    coords = [int(c) for c in line_s.split(",")]
    beacons[scanner].append(tuple(coords))

scanner_coords = dict()

# all scanner combinations
beacons_keys = list(beacons.keys())
for i1, scanner1 in enumerate(beacons_keys):
    for i2 in range(i1 + 1, len(beacons)):
        scanner2 = beacons_keys[i2]

        differences = defaultdict(list)

        # all beacon combinations
        for isb1, scanner1_beacon in enumerate(beacons[scanner1]):
            for isb2 in range(isb1 + 1, len(beacons[scanner2])):
                scanner2_beacon = beacons[scanner2][isb2]

                x1, y1, z1 = scanner1_beacon
                for x2, y2, z2 in orientations(scanner2_beacon):

                    differences[(x1 - x2, y1 - y2, z1 - z2,)].append(
                        (
                            scanner1_beacon,
                            scanner2_beacon,
                        ),
                    )
        for k, v in differences.items():
            overlap_beacons = len(v)
            if overlap_beacons >= 12:
                scanner_coords[(scanner1, scanner2)] = k

scanners_connected = scanner_coords.keys()
scanner_chain = [0]
for s1, s2 in scanners_connected:
    if s1 == scanner_chain[-1] and s2 not in scanner_chain:
        scanner_chain.append(s2)
    elif s2 == scanner_chain[-1] and s1 not in scanner_chain:
        scanner_chain.append(s1)

target_scanner_beacons = []
for i in range(len(scanner_chain) - 1, 1, -1):
    source_scanner = scanner_chain[i]
    target_scanner = scanner_chain[i - 1]
    if (source_scanner, target_scanner) in scanner_coords:
        coords_x, coords_y, coords_z = scanner_coords[(source_scanner, target_scanner)]
    else:
        coords_x, coords_y, coords_z = [
            -c for c in scanner_coords[(target_scanner, source_scanner)]
        ]

    source_scanner_beacons = target_scanner_beacons + beacons[source_scanner]
    target_scanner_beacons = [
        (x + coords_x, y + coords_y, z + coords_z) for x, y, z in source_scanner_beacons
    ]


print(f"scanners = {len(beacons)}")
print(f"beacons = {sum([len(b) for b in beacons.values()])}")

print("Scanner coordinates")
for k, v in scanner_coords.items():
    print(f"Scanner {k[1]} in scanner {k[0]} coords = {v}")
