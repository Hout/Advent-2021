import numpy as np

fish_lst = [int(f) for f in open("input_6.txt").readline().strip().split(",")]
fish_arr = np.array(fish_lst, dtype=np.short)

for i in range(256):
    fish_arr = np.add(fish_arr, -1)
    fish_arr[fish_arr == -1] = 8
    to_append = np.full_like(fish_arr[fish_arr == 8], fill_value=6, dtype=np.short)
    fish_arr = np.concatenate((fish_arr, to_append), axis=None)

    print(f"{i}: {fish_arr.shape[0]}")
