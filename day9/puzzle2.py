line = input()
garbage_count = 0

def calculate_score(string, start_pos, value):
    count  = 0
    running_pos = start_pos + 1
    garbage = False
    while True:
        # Ok, I will admit this line is kind of bad, but it gets it done with
        # minimum changes to the original code
        if garbage and string[running_pos] != "!" and string[running_pos] != ">":
                global garbage_count
                garbage_count += 1

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
print(garbage_count)
