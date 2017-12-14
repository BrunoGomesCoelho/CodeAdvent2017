numbers = [int(x) for x in input()]

size = len(numbers)
offset = size // 2

count = 0
for i in range(size):
    if numbers[i] == numbers[ (i+offset) % size ]:
        count += numbers[i]

print(count)



