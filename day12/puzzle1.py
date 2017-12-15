from collections import defaultdict

graph = defaultdict(set)

line = input()

def process_input(line):
    line = line.translate({ord(c): None for c in "<->,"}).split()
    return line[0], line[1:]

while line:
    father, neighbours = process_input(line)
    for v in neighbours:
        graph[father].add(v)

    line = input()

visited = set()

def dfs(visited, node):
    for v in graph[node]:
        if v not in visited:
            visited.add(v)
            dfs(visited, v)
dfs(visited, "0")

print(len(visited))



