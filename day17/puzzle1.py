# steps = 3
steps = 382

lst = [0]
current_pos = 0

for step in range(1, 2018):
    pos = (current_pos + steps + 1) % step
    lst.insert(pos, step)
    current_pos = pos 

print(lst[current_pos + 1])

