from collections import defaultdict

line = input().split(",")

def operators(cmd, n_count, ne_count, nw_count, s_count, se_count, sw_count):
    return {
        "n": lambda: (n_count + 1, ne_count, nw_count, s_count, se_count, sw_count), 
        "nw": lambda: (n_count, ne_count, nw_count + 1, s_count, se_count, sw_count), 
        "ne": lambda: (n_count, ne_count + 1, nw_count, s_count, se_count, sw_count),
        "s": lambda: (n_count, ne_count, nw_count, s_count + 1, se_count, sw_count),
        "sw": lambda: (n_count, ne_count, nw_count, s_count, se_count, sw_count + 1),   
        "se": lambda: (n_count, ne_count, nw_count, s_count, se_count + 1, sw_count),
    }.get(cmd, lambda: None)()

dic = defaultdict(int)
n_count, ne_count, nw_count = 0

for cmd in line:
    n_count, ne_count, nw_count, s_count, se_count, sw_count = \
            operators(cmd, n_count, ne_count, nw_count, s_count, se_count, sw_count)  

def change_min(a, b):
    smallest = min(a, b)
    return a - smallest, b -smallest, True

while True:
    change = False
    if n_count > 0 and s_count > 0:
            
    if ne_count > 0 and sw_count > 0:
        smallest = min(n_count, s_count)
        n_count -= smallest
        s_count -= smallest





