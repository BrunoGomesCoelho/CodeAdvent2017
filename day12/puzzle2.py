from collections import defaultdict

def process_input(line):
    line = line.translate({ord(c): None for c in "<->,"}).split()
    return line[0], line[1:]

def dfs(all_nodes, visited, node):
    if node in all_nodes:
        all_nodes.remove(node)

    for v in graph[node]:
        if v not in visited:
            visited.add(v)
            dfs(all_nodes, visited, v)
 
graph = defaultdict(set)

line = input()

while line:
    father, neighbours = process_input(line)
    for v in neighbours:
        graph[father].add(v)
    line = input()

all_nodes = [format("%d" % x) for x in range(len(graph))]
group_count = 0
visited = set()

while len(all_nodes) != 0:
    group_count += 1
    start = all_nodes[0]
    dfs(all_nodes, visited, start)

print(group_count)



