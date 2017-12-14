line = input()

def calculate_score(string, start_pos, value):
    count  = 0
    running_pos = start_pos + 1
    garbage = False
    while True:
        if string[running_pos] == "{" and not garbage:
            running_pos, temp = calculate_score(string, running_pos, value+1)
            count += temp
        elif string[running_pos] == "}" and not garbage:
            return running_pos+1, count + value
        elif string[running_pos] == "!":
            running_pos += 2
        else:
            if string[running_pos] == "<" and not garbage:
                garbage = True
            if string[running_pos] == ">" and garbage:
                garbage = False
            running_pos += 1

print(calculate_score(line, 0, 1)[1])

