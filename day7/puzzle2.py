from collections import defaultdict


def read_line():
    line = input()

    # ord is the int representation of the unicode character
    line = line.translate({ord(c): None for c in "()->,"})

    return line.split()

def dfs(node):
    if len(tree[node]) == 0:
        return weights[node]
    else:
        found = False
        values = []
        count = son_value = dfs(tree[node][0])
        values.append((son_value, tree[node][0]))

        for son in tree[node][1:]:
            value = dfs(son)
            count += value
            if value != son_value:
                found = True
            values.append((value, son))
        if found:
            values.sort()
            if values[0][0] != values[1][0]:
                print(values[0][1], ":", values[1][0]-values[0][0] + weights[values[0][1]])
            else:
                print(values[-1][1], ":", weights[values[-1][1]] - (values[-1][0] - values[-2][0]))
            exit(0)
        return count + weights[node]
            


tree = defaultdict(list)
weights = defaultdict(int)
    
childs = set()
possible_fathers = set()

line = read_line()

# Reads the input and creates the tree
while line:
    father, weight, sons = line[0], int(line[1]), line[2:]
    tree[father] = sons
    weights[father] = weight

    if father not in childs:
        possible_fathers.add(father)

    for son in sons:
        childs.add(son)
        possible_fathers.discard(son)

    line = read_line()

# Gets the root
root = None
for node in possible_fathers:
    root = node

# Peforms a DFS and finds out thw wrong weight
print(dfs(root))



