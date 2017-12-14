vector = [int(x) for x in input().split()]
count = 0
visited = set()
visited.add(tuple(vector))

mem_banks = 16

while True:
    count += 1
    biggest = max(vector)
    pos = vector.index(biggest)
    vector[pos] = 0
    for i in range(biggest):
        vector[ (pos+1+i) % mem_banks ] += 1
    tup = tuple(vector)
    if tup in visited:
        break
    else:
        visited.add(tup)

print(count)

    

