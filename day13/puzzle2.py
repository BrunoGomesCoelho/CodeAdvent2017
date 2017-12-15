from collections import defaultdict


def process_input(line):
    return map(int, line.split(": "))


def update_time(layers, vert, positions):
    for key in range(biggest+1):
        if layers[key] != -1 and vert[key] == "down":
            if positions[key] != layers[key] - 1:
                positions[key] += 1
            else:
                positions[key] -= 1
                vert[key] = "up"
        elif layers[key] != -1 and vert[key] == "up":
            if positions[key] != 0:
                positions[key] -= 1
            else:
                positions[key] += 1
                vert[key] = "down"

layers = defaultdict(lambda: -1)

biggest = 0
line = input()

# Reads input
while line:
    depth, size = process_input(line)
    layers[depth] = size
    biggest = max(biggest, depth)

    line = input()

direction = ["down" for _ in range(biggest+1)]
current_pos = [0 for _ in range(biggest+1)]

count = 0
while True:
    old_pos = [x for x in current_pos]
    old_direction = [x for x in direction]

    for i in range(biggest + 1):
        if layers[i] != -1 and current_pos[i] == 0:
            break
        else:
            update_time(layers, direction, current_pos)
    else:
        break
    count += 1
    update_time(layers, old_direction, old_pos)
    current_pos = old_pos
    direction = old_direction


print(count)
