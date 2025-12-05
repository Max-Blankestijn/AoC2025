with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

ranges = []
ingredients = []

passed = False
for line in lines:
    if not line:
        passed = True
        continue
    if passed:
        ingredients.append(int(line))
    else:
        ranges.append(line)

spoiled_items = 0
for ingredient in ingredients:
    spoiled = True
    for rng in ranges:
        lb, rb = [int(num) for num in rng.split("-")]
        if lb <= ingredient <= rb:
            spoiled = False
    if spoiled:
        spoiled_items += 1

print(spoiled_items)