def process_input():
    return [int(input().split()[4]) for _ in range(2)]

def convert_binary(nums):
    tmp = [format(num, "032b")[-16:] for num in nums]
    return tmp[0] == tmp[1]

def generate(num, key):
    return { 
            "a": 16807,
            "b": 48271
    }.get(key)*num % 2147483647


a_value, b_value = [722, 354]
# a_value, b_value = [65, 8921]
count = 0
a_lst = []
b_lst = []
limit = 5*10**6

while True:
    if len(a_lst) == limit and len(b_lst) == limit:
        break
    elif len(a_lst) < limit:
        while True:
            a_value = generate(a_value, "a")
            if a_value % 4 == 0:
                a_lst.append(a_value)
                break
    elif len(b_lst) < limit:
        while True:
            b_value = generate(b_value, "b")
            if b_value % 8 == 0:
                b_lst.append(b_value)
                break

for i in range(limit):
    if convert_binary([a_lst[i], b_lst[i]]):
        count += 1

print(count)

