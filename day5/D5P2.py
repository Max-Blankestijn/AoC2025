with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


intervals = []
passed = False

for line in lines:
    if not line:
        break
    if not passed:
        lb, rb = [int(num) for num in line.split("-")]
        intervals.append((lb, rb))

intervals.sort()
merged = []
current_start, current_end = intervals[0]

for start, end in intervals[1:]:
    if start <= current_end + 1:
        current_end = max(end, current_end)
    else:
        merged.append((current_start, current_end))
        current_start, current_end = start, end

merged.append((current_start, current_end))

fresh = sum([rng[1] - rng[0] + 1 for rng in merged])
print(fresh)
