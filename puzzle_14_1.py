# puzzle 14
from collections import Counter

lines = open("input_14.txt").readlines()

template = lines[0].strip()
pairs = [template[i : i + 2] for i in range(len(template) - 1)]
pair_counter = Counter(pairs)

instructions = {k: v for k, v in [line.strip().split(" -> ") for line in lines[2:]]}

for i in range(10):
    new_pair_counter = Counter()
    for pair, occurrences in pair_counter.items():
        insert_char = instructions[pair]
        new_pair_counter[pair[0] + insert_char] += occurrences
        new_pair_counter[insert_char + pair[1]] += occurrences
    pair_counter = new_pair_counter
    print(f"{i} - len = {sum(pair_counter.values())+1} - {pair_counter}")

char_counter = Counter()
for pair, occurrences in pair_counter.items():
    char_counter[pair[0]] += occurrences
char_counter[template[-1]] += 1

print(char_counter)
print(f"min = {min(char_counter.values())}")
print(f"max = {max(char_counter.values())}")
print(f"diff = {max(char_counter.values())-min(char_counter.values())}")
