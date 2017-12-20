def process_input():
    return [int(input().split()[4]) for _ in range(2)]

def convert_binary(nums):
    return [format(num, "032b")[-16:] for num in nums]

def generate(nums):
    multiply = [16807, 48271]
    mod = 2147483647
    return [nums[x]*multiply[x] % mod for x in range(2)]

nums = process_input()
# nums = [65, 8921]
count = 0

for _ in range(40*10**6):
    nums = generate(nums)
    bin_a, bin_b = convert_binary(nums)
    if bin_a == bin_b:
        count += 1
print(count)
