instruction_list = []
with open("input_2_1.txt") as f:
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        direction, steps = stripped_line.split()
        instruction_list.append((direction, int(steps)))

hor = 0
depth = 0
for direction, steps in instruction_list:
    if direction == "forward":
        hor += steps
        continue
    if direction == "up":
        depth -= steps
        continue
    if direction == "down":
        depth += steps
        continue

print(f"hor * depth = {hor*depth}")
