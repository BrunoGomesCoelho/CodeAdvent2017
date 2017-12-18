# Importing knot-hash from day 10
import sys
sys.path.append("../")

from day10.puzzle2 import knot_hash

def dfs(graph, row, col):
    if row < 0 or row >= 128 or col < 0 or col >= 128 or graph[row][col] == "0":
        return
    else:
        graph[row][col] = "0"
        dfs(graph, row-1, col)
        dfs(graph, row+1, col)
        dfs(graph, row, col-1)
        dfs(graph, row, col+1)


# input_string = "flqrgnkx" + "-"
input_string = "vbqugkhl" + "-"
graph = []

# Reads input
for i in range(128):
    txt = input_string + str(i) 
    numbers = knot_hash(txt)

    # creates the string format of the binary representation
    string_numbers = ""
    for num in numbers:
        string_numbers += format(num, "08b")
    
    """
    adds the row to the graph
    it is necessary to convert the whole string to a array to deal with the 
    fact that strings are imutable 
    """
    
    graph.append([x for x in string_numbers])

group_count = 0

# Peforms a DFS on grups, swapping 1 for 0 as we go
for i in range(128):
    for j in range(128):
        if graph[i][j] == "1":
            group_count += 1
            dfs(graph, i, j)

print(group_count)




