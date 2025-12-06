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
print(equations[0:10])
operator_idx = 0
total = 0
cur_equation = np.array([])

for i in range(len(equations)+2):
    numbers = np.diag(np.fliplr(equations), k=2-i)[::-1]
    numbers = numbers[numbers != " "]

    current_num = ""
    for number in numbers:
        current_num += number

    if current_num != "":
        cur_equation = np.append(cur_equation, current_num)

    if current_num == "":
        cur_equation = np.array([int(num) for num in cur_equation])
        if operators[operator_idx] == "*":
            total += np.product(cur_equation)
        else:
            total += np.sum(cur_equation)
        operator_idx += 1
        cur_equation = []

print(total)