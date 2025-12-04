from collections import defaultdict
from copy import deepcopy

with open("input.txt") as file:
    grid = [line.strip() for line in file.readlines()]

grid_points = defaultdict(str)

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        grid_points[x + 1j * y] = cell

grid = deepcopy(grid_points)
accesible = 0
removed = True

while removed:
    removed = False
    for key, value in grid.items():
        if value != "@":
            continue
        tp_count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i != 0 or j != 0) and grid_points[key + i + 1j * j] == "@":
                    tp_count += 1
        if tp_count < 4:
            accesible += 1
            grid_points[key] = "."
            removed = True
    grid = deepcopy(grid_points)

print(accesible)


