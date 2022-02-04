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


def deduct_digits(signal_patterns: list) -> dict:
    deducted = {}

    # determine unique lengths
    for p in signal_patterns:
        for k, v in unique_segment_length_digits.items():
            if len(p) == v:
                deducted[k] = p

    for p in signal_patterns:
        if p not in deducted.values():
            if len(p) == 5:
                # 3, 5, 2
                if p > deducted[1] and p > deducted[7]:
                    deducted[3] = p
                elif len(p & deducted[7]) == 2 and len(p & deducted[4]) == 3:
                    deducted[5] = p
                else:
                    deducted[2] = p
            else:
                # length 6: 6,9,0
                if len(p & deducted[1]) == 1:
                    deducted[6] = p
                elif deducted[4] < p:
                    deducted[9] = p
                else:
                    deducted[0] = p

    return deducted


total = 0
for line in open("input_8.txt"):
    stripped_line = line.strip()
    signal_patterns_txt, output_values_txt = stripped_line.split("|")
    signal_patterns = [set(p) for p in signal_patterns_txt.split()]
    output_values = [set(o) for o in output_values_txt.split()]

    deducted_digits = deduct_digits(signal_patterns)

    number = 0
    for o in output_values:
        for d, p in deducted_digits.items():
            if o == p:
                digit = d
                break
        number = 10 * number + digit

    print(number)
    total += number

print(total)
