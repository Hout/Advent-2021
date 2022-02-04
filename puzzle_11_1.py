octopusses = []
for line in open("input_11.txt"):
    octopusses.append([int(o) for o in line.strip()])


def upgrade(i, j):
    octopusses[i][j] += 1
    if octopusses[i][j] == 10:
        flash(i, j)


def upgrade_all():
    global octopusses
    for i in range(len(octopusses)):
        for j in range(len(octopusses[i])):
            upgrade(i, j)


def reset_flashed():
    global octopusses
    for i in range(len(octopusses)):
        for j in range(len(octopusses[i])):
            if octopusses[i][j] > 9:
                octopusses[i][j] = 0


def upgrade_adjacent(i: int, j: int):
    global octopusses

    for ia in range(i - 1, i + 2):
        if ia < 0 or ia >= len(octopusses):
            continue
        for ja in range(j - 1, j + 2):
            if ja < 0 or ja >= len(octopusses[ia]):
                continue
            if ia == i and ja == j:
                continue
            upgrade(ia, ja)


flashes = 0


def flash(i: int, j: int):
    global flashes

    flashes += 1
    upgrade_adjacent(i, j)


def synchronised() -> bool:
    for ol in octopusses:
        for o in ol:
            if o != 0:
                return False
    return True


for step in range(10 ** 9):
    upgrade_all()
    reset_flashed()

    print(f"After step {step+1}")
    for i in range(len(octopusses)):
        print("".join([str(o) for o in octopusses[i]]))
    print()

    if synchronised():
        print(f"Step {step+1}")
        break
