import numpy as np

with open("input.txt") as file:
    lines = [line.strip().split() for line in file.readlines()]

for j, row in enumerate(lines[:-1]):
    for i, num in enumerate(row):
        lines[j][i] = int(lines[j][i])

equations = np.array(lines[:-1], np.int64).T
operators = np.array(lines[-1])

total = 0

for idx, equation in enumerate(equations):
    if operators[idx] == "*":
        total += np.product(equation)
    else:
        total += np.sum(equation)

print(total)