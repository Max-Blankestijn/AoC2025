from functools import cache

with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

paths = {}
for line in lines:
    start, path = line.split(": ")
    paths[start] = path.split(" ")

@cache
def new_paths(path, dac, fft):
    if path == "dac":
        dac = True
    elif path == "fft":
        fft = True
    elif path == "out":
        if dac and fft:
            return 1
        else:
            return 0
    return sum((new_paths(cur_path, dac, fft) for cur_path in paths[path]))

count = new_paths("svr", False, False)
print(count)
