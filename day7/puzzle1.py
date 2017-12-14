def read_line():
    line = input()

    # ord is the int representation of the unicode character
    line = line.translate({ord(c): None for c in "()->,"})

    return line.split()
    
childs = set()
possible_fathers = set()

line = read_line()

while line:
    father, sons = line[0], line[2:]
    if father not in childs:
        possible_fathers.add(father)

    for son in sons:
        childs.add(son)
        possible_fathers.discard(son)

    line = read_line()

print(possible_fathers)
