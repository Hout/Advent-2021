import numpy as np


class Point:
    def __init__(self, x_init: int, y_init: int):
        if x_init is None:
            x_init = 0
        if y_init is None:
            y_init = 0
        self.x = x_init
        self.y = y_init

    def __repr__(self):
        return "".join(["Point(", str(self.x), ",", str(self.y), ")"])


class Line:
    def __init__(self, p1_init: Point, p2_init: Point):
        self.p1 = p1_init
        self.p2 = p2_init


class Area:
    def __init__(self, size_x: int, size_y: int):
        assert size_x > 0
        assert size_y > 0
        self.surface = np.zeros((size_x + 1, size_y + 1), dtype=np.short)

    def add_line(self, line: Line):
        x1 = min(line.p1.x, line.p2.x)
        x2 = max(line.p1.x, line.p2.x)
        y1 = min(line.p1.y, line.p2.y)
        y2 = max(line.p1.y, line.p2.y)
        if line.p1.x == line.p2.x:
            # horizontal
            x = line.p1.x
            for y in range(y1, y2 + 1):
                self.surface[x, y] += 1
        elif line.p1.y == line.p2.y:
            # vertical
            y = line.p1.y
            for x in range(x1, x2 + 1):
                self.surface[x, y] += 1
        else:
            assert False

    def high_points(self, threshold: int) -> int:
        return np.count_nonzero(self.surface > threshold)


lines = list()
max_x = 0
max_y = 0
for text_line in open("input_5t.txt").readlines():
    stripped_line = text_line.strip()
    if stripped_line == "":
        continue

    points = [
        Point(int(x), int(y))
        for x, y in [point.split(",") for point in stripped_line.split(" -> ")]
    ]
    max_x = max(max_x, points[0].x, points[1].x)
    max_y = max(max_y, points[0].y, points[1].y)
    lines.append(Line(points[0], points[1]))

area = Area(max_x, max_y)

for line in lines:
    area.add_line(line)

print(area.high_points(1))
