import numpy as np

# fish_lst = [int(f) for f in open("input_6.txt").readline().strip().split(",")]

d = {}

fish_arr = np.array([0], dtype=np.short)

for j in range(1, 257):
    fish_arr = np.add(fish_arr, -1)
    fish_arr[fish_arr == -1] = 8
    to_append = np.full_like(fish_arr[fish_arr == 8], fill_value=6, dtype=np.short)
    fish_arr = np.concatenate((fish_arr, to_append), axis=None)

    for i in range(9):
        d[(i, j + i)] = fish_arr.shape[0]
    print(f"{j} - {fish_arr.shape[0]}")

fish_lst = [int(f) for f in open("input_6.txt").readline().strip().split(",")]
result = 0
for f in fish_lst:
    result += d[(f, 256)]

print(result)
