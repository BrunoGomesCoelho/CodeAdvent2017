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


def cancel_equals(a, b):
    smallest = min(a, b)
    return a - smallest, b -smallest, True

def cancel_opposites(a, b):
    smallest = min(a, b)
    return smallest, a - smallest, b - smallest, True

def calculate_distance():
    global n_count, ne_count, nw_count, s_count, se_count, sw_count
    global maximum
    while True:
        change = False
        # cancels equal moves
        if n_count > 0 and s_count > 0:
               n_count, s_count, change =  cancel_equals(n_count, s_count)
        if ne_count > 0 and sw_count > 0:
            ne_count, sw_count, change =  cancel_equals(ne_count, sw_count)
        if nw_count > 0 and se_count > 0:
            nw_count, se_count, change =  cancel_equals(nw_count, se_count)
        
        # a diag right up + diag left up = up
        if ne_count > 0 and nw_count > 0:
            smallest, ne_count, nw_count, change = cancel_opposites(ne_count, nw_count)
            n_count += smallest
        # same thing down
        if se_count > 0 and sw_count > 0:
            smallest, se_count, sw_count, change = cancel_opposites(se_count, sw_count)
            s_count += smallest

        # n + se = ne
        if n_count > 0 and se_count > 0:
            smallest, n_count, se_count, change = cancel_opposites(n_count, se_count)
            ne_count += smallest
        # n + sw  = nw
        if n_count > 0 and sw_count > 0:
            smallest, n_count, sw_count, change = cancel_opposites(n_count, sw_count)
            nw_count += smallest   
        # s + nw = sw
        if s_count > 0 and nw_count > 0:
            smallest, s_count, nw_count, change = cancel_opposites(s_count, nw_count)
            sw_count += smallest  
        # s + ne = se
        if s_count > 0 and ne_count > 0:
            smallest, s_count, ne_count, change = cancel_opposites(s_count, ne_count)
            se_count += smallest  

        # if no change occured, abort
        if not change:
            break
    temp = sum([n_count, ne_count, nw_count, s_count, se_count, sw_count])
    if temp > maximum:
        maximum = temp

n_count = ne_count = nw_count = s_count = se_count = sw_count = 0
maximum = 0

for cmd in line:
    n_count, ne_count, nw_count, s_count, se_count, sw_count = \
            operators(cmd, n_count, ne_count, nw_count, s_count, se_count, sw_count)  
    calculate_distance()

print(maximum)
