with open("input.txt") as file:
    banks = [line.strip() for line in file.readlines()]

def find_largest(sub_str):
    largest = 0
    idx = 0
    for i, char in enumerate(sub_str):
        if int(char) > largest:
            largest = int(char)
            idx = i
    return idx + 1, largest

total_joltage = 0
active_batteries = 12

for bank in banks:
    joltage = ""
    idx = 0
    old_idx = 0
    for i in range(active_batteries):
        idx, num = find_largest(bank[idx:(None if (-active_batteries + i + 1) == 0 else -active_batteries + i + 1)])
        idx = old_idx + idx
        joltage += str(num)
        old_idx = idx
    total_joltage += int(joltage)

print(total_joltage)