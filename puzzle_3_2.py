import numpy as np

rows = list()
with open("input_3.txt") as f:
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        rows.append(list(stripped_line))

matrix = np.array(rows, dtype=np.short)

mask = [True] * matrix.shape[0]
for col in range(matrix.shape[1]):
    filtered = 0
    col_sum = np.sum(matrix[mask], axis=0)[col]
    filter_value = 1 if col_sum >= (matrix[mask].shape[0] / 2) else 0
    for row in range(len(mask)):
        mask[row] = mask[row] and matrix[row, col] == filter_value
    if matrix[mask].shape[0] == 1:
        break

oxygen_lst = matrix[mask][0].tolist()
oxygen_str = "".join(map(lambda b: "1" if b == 1 else "0", oxygen_lst))
oxygen_value = int(oxygen_str, 2)
print(f"oxygen = {oxygen_value}")

mask = [True] * matrix.shape[0]
for col in range(matrix.shape[1]):
    filtered = 0
    col_sum = np.sum(matrix[mask], axis=0)[col]
    filter_value = 1 if col_sum < (matrix[mask].shape[0] / 2) else 0
    for row in range(len(mask)):
        mask[row] = mask[row] and matrix[row, col] == filter_value
    if matrix[mask].shape[0] == 1:
        break

co2_lst = matrix[mask][0].tolist()
co2_str = "".join(map(lambda b: "1" if b == 1 else "0", co2_lst))
co2_value = int(co2_str, 2)
print(f"co2 = {co2_value}")

print(f"Solution = {oxygen_value*co2_value}")
