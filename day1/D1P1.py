with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

dial = 50
zero_count = 0
for line in lines:
    direction = {"L": -1, "R": 1}[line[0]]
    amount = int(line[1:])
    dial = (dial + amount * direction) % 100

    if dial == 0:
        zero_count += 1

print(zero_count)