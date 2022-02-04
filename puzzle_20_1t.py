conv = {".": 0, "#": 1}
progin = open("input_20t.txt").read().split("\n\n")[0]
prog = [i for i in range(len(progin)) if progin[i] == "#"]
pixelsin = open("input_20t.txt").read().split("\n\n")[1].split("\n")
space = {
    complex(i, j): conv[pixelsin[j][i]]
    for j in range(len(pixelsin))
    for i in range(len(pixelsin[0]))
}


def flatten(center, space, rnd):
    default = str(
        (rnd + 1) % 2
    )  # for the input with the alternative flashing at infinity
    middlerow = [center - 1, center, center + 1]
    locs = [x - 1j for x in middlerow] + middlerow + [x + 1j for x in middlerow]
    num = ""
    for z in locs:
        if z in space:
            num += str(space[z])
        else:
            num += default
    return int(num, 2)


def pad(space, default):
    reals, imags = [int(z.real) for z in space.keys()], [
        int(z.imag) for z in space.keys()
    ]
    left, right, up, down = min(reals), max(reals), min(imags), max(imags)
    padding = [
        complex(x, y) for x in range(left - 2, left) for y in range(up - 2, down + 3)
    ]  # left
    padding += [
        complex(x, y)
        for x in range(right + 1, right + 3)
        for y in range(up - 2, down + 3)
    ]  # right
    padding += [
        complex(x, y) for x in range(left - 2, right + 3) for y in range(up - 2, up)
    ]  # top
    padding += [
        complex(x, y)
        for x in range(left - 2, right + 3)
        for y in range(down + 1, down + 3)
    ]  # bottom
    for p in padding:
        if p not in space:
            space[p] = default
    return space


space = pad(space, 0)
rounds = 50
for rnd in range(1, rounds + 1):
    newspace = {}
    for z in space:
        if flatten(z, space, rnd) in prog:
            newspace[z] = 1
        else:
            newspace[z] = 0
    space = pad(newspace, rnd % 2)
print(sum(space.values()))
