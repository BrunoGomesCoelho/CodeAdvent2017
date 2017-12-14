vector = []
line = input()

while line:
    vector.append(int(line))
    line = input()

pos = 0
size = len(vector)
count = 0

while True:
    if 0 <= pos < size:
        old_value = vector[pos]
        if old_value >= 3:
            vector[pos] -= 1
        else:
            vector[pos] += 1

        pos += old_value
        count += 1
    else:
        break

print(count)

