import numpy as np

with open("sample.txt") as file:
    lines = [line.strip() for line in file.readlines()]

char_array = [list(line) for line in lines]
max_len = max(len(row) for row in char_array)

for i, row in enumerate(char_array):
    if len(row) != max_len:
        char_array[i].append(" ")

trans_array = np.transpose(char_array)

equations = np.array(trans_array)[:, :-1]
operators = lines[-1].split()

operator_idx = 0
total = 0
cur_equation = np.array([])

for equation in equations:
    current_num = ""
    for num in equation:
        if num != " ":
            current_num += num

    if current_num != "":
        cur_equation = np.append(cur_equation, int(current_num))
    else:
        if operators[operator_idx] == "*":
            total += np.product(cur_equation)
        else:
            total += np.sum(cur_equation)

        operator_idx += 1
        cur_equation = np.array([])

if operators[operator_idx] == "*":
    total += np.product(cur_equation)
else:
    total += np.sum(cur_equation)

print(total)