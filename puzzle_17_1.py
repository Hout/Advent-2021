import re

lines = open("input_17.txt").read().splitlines()
for line in lines:
    m = re.match(
        r"target area: x=([+-]?\d+)..([+-]?\d+), y=([+-]?\d+)..([+-]?\d+)", line
    )
    x1 = int(m.group(1))
    x2 = int(m.group(2))
    y1 = int(m.group(3))
    y2 = int(m.group(4))

    height = y2 - y1 + 1
    width = x2 - x1 + 1
    distance_x = x1 + width / 2

    assert x1 > 0 or x2 < 0
    x1a = abs(x1)
    x2a = abs(x2)

    # calculate horizontal speed
    # add up numbers in range(i) until we passed x2
    x = 0
    hv = 0
    hv_set = set()
    while x <= x2a:
        if x >= x1a:
            hv_set.add(hv)
        hv += 1
        x += hv
    if hv_set == []:
        # not found
        print("No feasible solution")

    print(f"hv = {hv_set}")

    # calculate evertical speed
    # to be as high as possible it should end with maximum the height of the target area
    # as negative of course, and after the horizontal speed has worn out

    # vv should be equal to height while travelling through area y range, then return
    vv_set = set()
    for start_vv in range(min(hv_set), height - y1):
        y = 0
        vv = start_vv
        # first go up
        while y < y2:
            y += vv
            vv -= 1
        # then come down
        while y >= y1:
            if y <= y2:
                vv_set.add(start_vv)
            y += vv
            vv -= 1

    print(f"vv = {vv_set}")

    # final check
    successes = []
    for start_hv in hv_set:
        for start_vv in vv_set:
            positions = []
            position = (0, 0)
            hv = start_hv
            vv = start_vv
            while position[0] < x2 and (vv > 0 or position[1] >= y1):
                positions.append(position)
                if (
                    position[0] >= x1
                    and position[0] <= x2
                    and position[1] >= y1
                    and position[1] <= y2
                ):
                    successes.append(
                        (start_hv, start_vv, positions, max([p[1] for p in positions]))
                    )

                position = (position[0] + hv, position[1] + vv)
                if hv > 0:
                    hv -= 1
                elif hv < 0:
                    hv += 1
                vv -= 1

    max_height = max([s[3] for s in successes])
    print(max_height)
    for success in successes:
        if success[3] == max_height:
            print(success)
