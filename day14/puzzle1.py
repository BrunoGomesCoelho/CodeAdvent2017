# Importing knot-hash from day 10
import sys
sys.path.append("../")

from day10.puzzle2 import knot_hash


# input_string = "flqrgnkx" + "-"
input_string = "vbqugkhl" + "-"
used_count = 0

for i in range(128):
    txt = input_string + str(i) 

    row_hash = knot_hash(txt)

    for num in row_hash:
        used_count += bin(num).count("1")

print(used_count)




