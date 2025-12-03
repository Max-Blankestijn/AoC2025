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


joltage = 0
for bank in banks:
    idx1, num1 = find_largest(bank[:-1])
    idx2, num2 = find_largest(bank[idx1:])
    joltage += int(str(num1) + str(num2))

print(joltage)