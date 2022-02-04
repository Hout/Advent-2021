with open("input_1_1.txt") as f:
    counter_list = []
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        current_number = int(stripped_line)
        counter_list.append(current_number)


previous_number = 99999
counter = 0
for i in range(2, len(counter_list)):
    sum3 = counter_list[i - 2] + counter_list[i - 1] + counter_list[i]
    if sum3 > previous_number:
        counter += 1
    previous_number = sum3

print(counter)
