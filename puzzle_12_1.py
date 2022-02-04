from collections import defaultdict
from copy import deepcopy

connections = defaultdict(list)


def get_data():
    global connections

    connection_lst = [
        line.split("-")
        for line in [line.strip() for line in open(r"input_12.txt", "r")]
    ]

    connection_dict = defaultdict(set)
    for c in connection_lst:
        connection_dict[c[0]].add(c[1])
        connection_dict[c[1]].add(c[0])

    connections = {k: list(v) for k, v in connection_dict.items()}


def is_small_cave(node: str) -> bool:
    return not node.isupper()


def get_paths_from(path: list[str], paths: list[list[str]]) -> list[list[str]]:
    global connections

    if path[-1] == "end":
        return paths

    for to_node in connections[path[-1]]:
        new_path = path + [to_node]
        if new_path in paths:
            continue
        if is_small_cave(to_node) and to_node in path:
            continue
        paths = get_paths_from(new_path, paths + [new_path])

    return paths


def get_paths() -> list[list[str]]:
    paths = get_paths_from(["start"], [["start"]])
    return [p for p in paths if p is not None and len(p) > 0 and p[-1] == "end"]


if __name__ == "__main__":
    get_data()
    paths = get_paths()
    print(paths)
    print(len(paths))
