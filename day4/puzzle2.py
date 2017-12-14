def read_input():
    return input()

line = read_input()
count = 0

while line:
    lst = []
    valid = True
    for x in line.split():
        s = set([letter for letter in x])
        if s in lst:
            valid = False
            break
        else:
            lst.append(s)
    if valid:
        count += 1

    line = read_input()
    
print(count)


