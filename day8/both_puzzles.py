from collections import defaultdict

def split_input(phrase):
    words = phrase.split()
    return (*words[0:2], int(words[2]), *words[4:6], int(words[6]))

# pythonic way of emulating a swithc statement
def operators(cmd, x, y):
    return {
        "<": lambda: x < y,
        "<=": lambda: x <= y,
        ">": lambda: x > y,
        ">=": lambda: x >= y,
        "==": lambda: x == y,
        "!=": lambda: x != y,

        # these two are used for the regs new value
        "inc": lambda: x + y,
        "dec": lambda: x - y,
    }.get(cmd, lambda: None)()


registers = defaultdict(int)

line = input()
count = 0

while line:
    reg, cmd, value, cond_reg, cond_cmd, cond_value = split_input(line)
    if operators(cond_cmd, registers[cond_reg], cond_value):
        registers[reg] =  operators(cmd, registers[reg], value)
        if registers[reg] > count:
            count = registers[reg]
    
    line = input()

print("Answer to first puzzle: ", max(registers.values()))
print("Answer to second puzzle: ", count)

