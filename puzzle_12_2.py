from collections import defaultdict, Counter
from typing import TypedDict


class Connections(TypedDict):
    from_node: str
    to_node: str


def get_data() -> Connections:
    connection_lst = [
        line.split("-")
        for line in [line.strip() for line in open(r"input_12.txt", "r")]
    ]

    connection_dict = defaultdict(set)
    for c in connection_lst:
        if c[1] != "start" and c[0] != "end":
            connection_dict[c[0]].add(c[1])
        if c[0] != "start" and c[1] != "end":
            connection_dict[c[1]].add(c[0])

    return {k: list(v) for k, v in connection_dict.items()}


def get_paths(connections: Connections, node: str, visited: list) -> list:
    paths = []
    new_path = visited + [node]
    if node == "end":
        return [new_path]

    for next in connections[node]:
        if next.isupper():
            temp_paths = get_paths(connections, next, new_path)
            paths.extend(temp_paths)
        else:
            node_counter = Counter([n for n in new_path if n.islower()])
            frequency_counter = Counter(node_counter.values())
            if frequency_counter[2] > 1:
                continue
            if not set(frequency_counter.keys()).issubset({1, 2}):
                continue

            temp_paths = get_paths(connections, next, new_path)
            paths.extend(temp_paths)

    return paths


if __name__ == "__main__":
    connections = get_data()
    paths = get_paths(connections, "start", [])
    paths.sort()
    for path in paths:
        print(",".join(path))
    print(len(paths))
