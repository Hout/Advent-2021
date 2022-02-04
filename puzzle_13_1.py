from typing import Tuple, List

Dots = List[Tuple[int, int]]


def get_data():
    dots = []
    folds = []

    for line in open("input_13t.txt"):
        if line.strip() == "":
            continue

        if line.startswith("fold along"):
            fold_direction, fold_value = line.strip().split()[2].split("=")
            folds.append((fold_direction, int(fold_value)))
            continue

        x, y = line.strip().split(",")
        dots.append((int(x), int(y)))

    return dots, folds


def print_dots(dots: Dots):
    max_x = max([x for x, _ in dots])
    max_y = max([y for _, y in dots])

    strings = ["".join(["." * (max_x + 1)])] * (max_y + 1)
    for x, y in dots:
        strings[y] = strings[y][:x] + "#" + strings[y][x + 1 :]
    for s in strings:
        print(s)

    print(f"Dot count = {len(dots)}")


def fold_along(direction: str, value: int, dots: Dots):
    index_position = {"x": 0, "y": 1}[direction]
    for i, dot in enumerate(dots):
        if dot[index_position] > value:
            new_dot = list(dot)
            new_dot[index_position] = 2 * value - dot[index_position]
            dots[i] = tuple(new_dot)
        elif dot[index_position] == value:
            del dots[i]
    # make dots unique
    return list(set(dots))


def main():
    dots, folds = get_data()
    print_dots(dots)
    for direction, value in [folds[0]]:
        dots = fold_along(direction=direction, value=value, dots=dots)
    print_dots(dots)


if __name__ == "__main__":
    main()
