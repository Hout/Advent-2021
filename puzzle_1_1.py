with open("input_1_1.txt") as f:
    counter = 0
    previous_number = 99999
    for line in iter(f.readline, ""):
        stripped_line = line.strip()
        current_number = int(stripped_line)
        if current_number > previous_number:
            counter += 1
        previous_number = current_number
    print(counter)
