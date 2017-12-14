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
        vector[pos] += 1
        if vector[pos] != 1:    # we have already summed 1
            pos += vector[pos] - 1
        count += 1
    else:
        break

print(count)

