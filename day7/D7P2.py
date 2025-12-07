with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

key_points = {}
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char != ".":
            key_points[i + 1j * j] = char
            if char == "S":
                start = i + 1j * j

beams = {start+1j: 1}
new_beams = {}
count = 0

while beams:
    for beam, value in beams.items():
        for j in range(len(lines)):
            if beam + 1j * j in key_points:
                if beam + 1j * j + 1 not in new_beams:
                    new_beams[beam + 1j * j + 1] = value
                else:
                    new_beams[beam + 1j * j + 1] += value
                if beam + 1j * j - 1 not in new_beams:
                    new_beams[beam + 1j * j - 1] = value
                else:
                    new_beams[beam + 1j * j - 1] += value
                break
            if j == len(lines)-1:
                count += value
    beams = new_beams
    new_beams = {}

print(count)