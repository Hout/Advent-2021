from typing import DefaultDict


digits = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg"),
}

segments = {k: len(v) for k, v in digits.items()}
length_digits = DefaultDict(list)
for k, v in segments.items():
    length_digits[v].append(k)
unique_segment_length_digits = {
    v[0]: k for k, v in length_digits.items() if len(v) == 1
}
unique_segment_lengths = set(unique_segment_length_digits.values())

count = 0
for line in open("input_8.txt"):
    stripped_line = line.strip()
    signal_patterns_txt, output_values_txt = stripped_line.split("|")
    signal_patterns = signal_patterns_txt.split()
    output_values = output_values_txt.split()

    for v in output_values:
        if len(v) in unique_segment_lengths:
            count += 1

print(count)
