def read_input():
    return input()

line = read_input()
count = 0

while line:
    s = set()
    valid = True
    for x in line.split():
        if x in s:
            valid = False
            break
        else:
            s.add(x)
    if valid:
        count += 1
    line = read_input()
    
print(count)


