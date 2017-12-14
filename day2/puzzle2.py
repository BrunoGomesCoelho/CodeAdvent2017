# For this to work, add a blank line at the end of the input.

def read_input():
    return sorted([ int(x) for x in input().split()], reverse=True)

line = read_input()
count = 0

while line:
    found = False
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            print("comapring %d to %d\n, division is %f" % (line[i], line[j], line[i] / line[j])) 
            if line[i] % line[j] == 0:
                count += line[i] // line[j]

    print("\n\n")
    
    line = read_input()

print(count)

