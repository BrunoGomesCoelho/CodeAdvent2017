print("Just a warning, this takes about 30 seconds to run")

steps = 382
CICLES = 50*10**6

current_pos = 0
zero_pos = 0
number_afer_zero = None

""" 
We must mantain the first value in the list in case 0 is the last value.
Actually, I think this will always be the case due to shenanigans in the
input. Very intelligente of the creators.
"""
begining_list = 0

for step in range(1, CICLES + 1):
    pos = (current_pos + steps + 1) % step 
    if pos == 0:
        begining_list = step
    if pos <= zero_pos:
        zero_pos += 1
    elif pos == zero_pos + 1:
        number_afer_zero = step
        zero_pos += 1
    current_pos = pos 

if number_afer_zero is not None:
    print(number_afer_zero)
else:
    print(begining_list)

