with open("input.txt") as file:
    range_str = [line.strip() for line in file.readlines()][0]

range_lst = range_str.split(",")
count = 0

for ID_range in range_lst:
    start, end = ID_range.split("-")
    IDs = range(int(start), int(end)+1)
    for ID in IDs:
        str_ID = str(ID)
        length = len(str_ID)
        sequence = ""
        for char in str_ID[:-1]:
            sequence += char
            if length / len(sequence) % 1 == 0 and sequence * (int(length / len(sequence))) == str_ID:
                count += ID
                break

print(count)
