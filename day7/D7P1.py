with open("input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

key_points = {}
for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char != ".":
            key_points[i + 1j * j] = char
            if char == "S":
                start = i + 1j * j

beams = [start+1j]
new_beams = []
split = {}
count = 0

while beams:
    for i, beam in enumerate(beams):
        for j in range(len(lines)):
            if beam + 1j * j in key_points:
                if beam + 1j * j not in split:
                    count += 1
                split[beam + 1j * j] = 1
                if beam + 1j * j + 1 not in new_beams:
                    new_beams.append(beam + 1j * j + 1)
                if beam + 1j * j - 1 not in new_beams:
                    new_beams.append(beam + 1j * j - 1)
                break
    beams = new_beams
    new_beams = []

print(count)