# For this to work, add a blank line at the end of the input.

def read_input():
    return [ int(x) for x in input().split()]

line = read_input()
count = 0

while line:
    count += max(line) - min(line)
    line = read_input()

print(count)

