# from collections import defaultdict
import numpy as np

rows = list()
with open("input_3.txt") as f:
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        rows.append(list(stripped_line))

matrix = np.array(rows, dtype=np.short)
col_sum = np.sum(matrix, axis=0)
gamma_str = "".join(
    list(map(lambda s: "1" if s >= matrix.shape[0] // 2 else "0", list(col_sum)))
)

gamma = int(gamma_str, 2)
epsilon = 2 ** matrix.shape[1] - 1 - gamma
power_consumption = gamma * epsilon
print(f"power consumption = {power_consumption}")
