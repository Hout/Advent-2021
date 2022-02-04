import re
from typing import List


class Coord:
    def __init__(self, x, y, z):
        self.x = x if type(x) == "int" else int(x)
        self.y = y if type(y) == "int" else int(y)
        self.z = z if type(z) == "int" else int(z)


class CoordRange:
    def __init__(self, coord1: Coord, coord2: Coord):
        assert coord1.x <= coord2.x
        assert coord1.y <= coord2.y
        assert coord1.z <= coord2.z
        self.coord1 = coord1
        self.coord2 = coord2

    def volume(self) -> int:
        return (
            (self.coord2.x - self.coord1.x)
            * (self.coord2.y - self.coord1.y)
            * (self.coord2.z - self.coord1.z)
        )


CoordRanges = List[CoordRange]


def intersect(cr1: CoordRange, cr2: CoordRange) -> bool:
    if cr1.coord1.x > cr2.coord2.x:
        return False
    if cr1.coord1.y > cr2.coord2.y:
        return False
    if cr1.coord1.z > cr2.coord2.z:
        return False
    if cr1.coord2.x < cr2.coord1.x:
        return False
    if cr1.coord2.y < cr2.coord1.y:
        return False
    if cr1.coord2.z < cr2.coord1.z:
        return False
    return True


def intersection(cr1: CoordRange, cr2: CoordRange) -> CoordRange:
    assert intersect(cr1, cr2)

    return CoordRange(
        Coord(
            max(cr1.coord1.x, cr2.coord1.x),
            max(cr1.coord1.y, cr2.coord1.y),
            max(cr1.coord1.z, cr2.coord1.z),
        ),
        Coord(
            min(cr1.coord2.x, cr2.coord2.x),
            min(cr1.coord2.y, cr2.coord2.y),
            min(cr1.coord2.z, cr2.coord2.z),
        ),
    )


def add(cr1: CoordRange, cr2: CoordRange) -> CoordRanges:
    if not intersect(cr1, cr2):
        return [cr1, cr2]

    return [subtract(cr1, intersection(cr1, cr2)), cr2]


def subtract(cr_on: CoordRange, cr_off: CoordRange) -> CoordRanges:
    x_ranges = []
    if cr_off.coord1.x > cr_on.coord1.x:
        x_ranges.append((cr_on.coord1.x, min(cr_on.coord2.x, cr_off.coord1.x)))
    if cr_off.coord2.x < cr_on.coord2.x:
        x_ranges.append((max(cr_on.coord1.x, cr_off.coord2.x)))
    if len(x_ranges) == 0:
        return

    y_ranges = []
    if cr_off.coord1.y > cr_on.coord1.y:
        y_ranges.append((cr_on.coord1.y, min(cr_on.coord2.y, cr_off.coord1.y)))
    if cr_off.coord2.y < cr_on.coord2.y:
        y_ranges.append((max(cr_on.coord1.y, cr_off.coord2.y)))
    if len(y_ranges) == 0:
        return [cr_on]

    z_ranges = []
    if cr_off.coord1.z > cr_on.coord1.z:
        z_ranges.append((cr_on.coord1.z, min(cr_on.coord2.z, cr_off.coord1.z)))
    if cr_off.coord2.z < cr_on.coord2.z:
        z_ranges.append((max(cr_on.coord1.z, cr_off.coord2.z)))
    if len(z_ranges) == 0:
        return [cr_on]

    result = CoordRanges()
    for x_range in x_ranges:
        for y_range in y_ranges:
            for z_range in z_ranges:
                result.append(
                    CoordRange(
                        Coord(
                            x_range.coord1.x,
                            x_range.coord1.y,
                            x_range.coord1.z,
                        ),
                        Coord(
                            x_range.coord2.x,
                            x_range.coord2.y,
                            x_range.coord2.z,
                        ),
                    )
                )


class Instruction:
    def __init__(self, status, coord_range: CoordRange):
        self.status = 1 if status == "on" else 0
        self.coord_range = coord_range


class Cuboid:
    def __init__(self, limits: CoordRange = None):
        self.instructions = []
        self.limits = limits

    def append(self, instruction: Instruction):
        if instruction.coord_range.coord2.x < self.limits.coord1.x:
            return
        if instruction.coord_range.coord2.y < self.limits.coord1.y:
            return
        if instruction.coord_range.coord2.z < self.limits.coord1.z:
            return
        if instruction.coord_range.coord1.x > self.limits.coord2.x:
            return
        if instruction.coord_range.coord1.y > self.limits.coord2.y:
            return
        if instruction.coord_range.coord1.z > self.limits.coord2.z:
            return

        if instruction.coord_range.coord1.x < self.limits.coord1.x:
            instruction.coord_range.coord1.x = self.limits.coord1.x
        if instruction.coord_range.coord1.y < self.limits.coord1.y:
            instruction.coord_range.coord1.y = self.limits.coord1.y
        if instruction.coord_range.coord1.z < self.limits.coord1.z:
            instruction.coord_range.coord1.z = self.limits.coord1.z
        if instruction.coord_range.coord2.x > self.limits.coord2.x:
            instruction.coord_range.coord2.x = self.limits.coord2.x
        if instruction.coord_range.coord2.y > self.limits.coord2.y:
            instruction.coord_range.coord2.y = self.limits.coord2.y
        if instruction.coord_range.coord2.z > self.limits.coord2.z:
            instruction.coord_range.coord2.z = self.limits.coord2.z

        self.instructions.append(instruction)

    def cube_status(self, coord: Coord) -> bool:
        result = 0
        for instruction in self.instructions:
            if coord.x < instruction.coord_range.coord1.x:
                continue
            if coord.x > instruction.coord_range.coord2.x:
                continue
            if coord.y < instruction.coord_range.coord1.y:
                continue
            if coord.y > instruction.coord_range.coord2.y:
                continue
            if coord.z < instruction.coord_range.coord1.z:
                continue
            if coord.z > instruction.coord_range.coord2.z:
                continue
            result = instruction.status
        assert result in {0, 1}
        return result

    def coord_range_status(self, coord_range: CoordRange = None) -> int:
        if coord_range is None:
            coord_range = self.limits
        result = 0
        for x in range(coord_range.coord1.x, coord_range.coord2.x + 1):
            for y in range(coord_range.coord1.y, coord_range.coord2.y + 1):
                for z in range(coord_range.coord1.z, coord_range.coord2.z + 1):
                    result += cuboid.cube_status(Coord(x, y, z))
        return result


cuboid = Cuboid(CoordRange(Coord(-50, -50, -50), Coord(50, 50, 50)))

for line in open("input_22_1.txt"):
    m = re.match(
        r"(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)", line
    )
    status, x1, x2, y1, y2, z1, z2 = m.groups()
    cuboid.append(Instruction(status, CoordRange(Coord(x1, y1, z1), Coord(x2, y2, z2))))

print(cuboid.coord_range_status())
