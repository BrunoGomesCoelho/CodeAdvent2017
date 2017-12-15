from collections import defaultdict

layers = defaultdict(lambda: -1)

def process_input(line):
    return map(int, line.split(": "))

biggest = 0
cost = 0
line = input()

while line:
    depth, size = process_input(line)
    layers[depth] = size
    biggest = max(biggest, depth)

    line = input()

direction = ["down" for _ in range(biggest+1)]
current_pos = [0 for _ in range(biggest+1)]

for i in range(biggest + 1):
    print(current_pos)
    print(direction)
    if layers[i] != -1 and current_pos[i] == 0:
        cost += i*layers[i]
    for key in range(biggest+1):
        if layers[key] != -1 and direction[key] == "down":
            if current_pos[key] != layers[key] - 1:
                current_pos[key] += 1
            else:
                current_pos[key] -= 1
                direction[key] = "up"
        elif layers[key] != -1 and direction[key] == "up":
            if current_pos[key] != 0:
                current_pos[key] -= 1
            else:
                current_pos[key] += 1
                direction[key] = "down"
print(cost)
