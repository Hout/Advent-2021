instruction_list = []
with open("input_2_1.txt") as f:
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        direction, steps = stripped_line.split()
        instruction_list.append((direction, int(steps)))

hor = 0
depth = 0
aim = 0
for direction, steps in instruction_list:
    if direction == "forward":
        hor += steps
        depth += aim * steps
        continue
    if direction == "up":
        aim -= steps
        continue
    if direction == "down":
        aim += steps
        continue

print(f"hor * depth = {hor*depth}")
