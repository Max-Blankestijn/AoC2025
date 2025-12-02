with open("input.txt") as file:
    range_str = [line.strip() for line in file.readlines()][0]

range_lst = range_str.split(",")
count = 0

for ID_range in range_lst:
    start, end = ID_range.split("-")
    IDs = range(int(start), int(end)+1)
    for ID in IDs:
        length = len(str(ID))
        if length % 2 == 1:
            continue
        else:
            if str(ID)[:int(length/2)] == str(ID)[int(length/2):]:
                count += int(ID)

print(count)