size = 16

start = ord("a")
programs = [chr(x) for x in range(start, start+size)]

cmds = input().split(",")

for cmd in cmds:
    if cmd[0] == "s":
        spin = int(cmd[1:])
        programs = programs[size-spin:] + programs[0:size-spin]
    elif cmd[0] == "x":
        pos_a, pos_b = map(int, cmd[1:].split("/"))
        programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]
    elif cmd[0] == "p":
        pos_a, pos_b = map(lambda x: programs.index(x), [cmd[1], cmd[3]])
        programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]

for letter in programs:
    print(letter, end="")
print("\n")
