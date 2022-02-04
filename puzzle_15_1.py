from collections import defaultdict, deque
from functools import reduce
from typing import DefaultDict, List, Tuple, Dict

Point = Tuple[int, int]
Path = List[Point]
Graph = List[List[int]]

graph: Graph = [
    [int(x) for x in line] for line in open("input_15.txt").read().splitlines()
]


def manhattan_distance(point: Point) -> int:
    """manhattan distance to goal"""
    return len(graph) - point[1] + len(graph[0]) - point[0]


def neighbours(node: Point):
    if node[0] > 0:
        yield (node[0] - 1, node[1])
    if node[0] < len(graph[0]) - 1:
        yield (node[0] + 1, node[1])
    if node[1] > 0:
        yield (node[0], node[1] - 1)
    if node[1] < len(graph) - 1:
        yield (node[0], node[1] + 1)


def reconstruct_path(came_from: Dict[Point, Point], current: Point):
    total_path = deque([current])
    while current in came_from.keys():
        current = came_from[current]
        total_path.appendleft(current)
    return total_path


def a_star(from_point: Point, to_point: Point) -> Path:
    high_value = 9999999999

    open_set = {from_point}
    came_from = dict()

    g_score = defaultdict(lambda: high_value)
    g_score[from_point] = 0

    f_score = defaultdict(lambda: high_value)
    f_score[from_point] = manhattan_distance(from_point)

    while open_set != {}:
        # find node in open_set with lowest f_score
        current = reduce(
            lambda p, c: c if f_score[p] > f_score[c] else p, open_set, None
        )
        if current == to_point:
            return reconstruct_path(came_from, current)
        open_set.remove(current)
        for neighbour in neighbours(current):
            tentative_g_score = g_score[current] + graph[neighbour[1]][neighbour[0]]
            if tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + 1
                open_set.add(neighbour)
    return None


path = a_star((0, 0), (len(graph[0]) - 1, len(graph) - 1))
print(path)
print(reduce(lambda p, c: p + graph[c[1]][c[0]], list(path)[1:], 0))
