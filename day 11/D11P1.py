with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

paths = {}
for line in lines:
    start, path = line.split(": ")
    paths[start] = path.split(" ")

count = 0
cur_paths = paths["you"]
new_paths = []

while cur_paths:
    for path in cur_paths:
        if path == "out":
            count += 1
            continue
        for new_path in paths[path]:
            new_paths.append(new_path)
    cur_paths = new_paths
    new_paths = []

print(count)
