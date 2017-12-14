numbers = [int(x) for x in input()]

count = 0
for i in range(len(numbers)-1):
    if numbers[i] == numbers[i+1]:
        count += numbers[i]

if numbers[0] == numbers[-1]:
    count += numbers[0]

print(count)



