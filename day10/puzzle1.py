from itertools import cycle

size = 256
lst = [x for x in range(size)]

line = map(int, input().split(","))
skip_size = 0
pos = 0

for lenght in line:
    end = (pos - 1 + lenght) % size
    for i in range(0, lenght // 2):
        lst[(pos + i) % size], lst[(end - i) % size] = \
            lst[(end - i) % size], lst[(pos + i) % size]
    pos = (lenght + skip_size + pos) % size
    skip_size += 1

print(lst[0]*lst[1])
