"""
For this one we use a completely different stategy: actually create
the matrix and populate it
"""

def process_move(move, x, y):
    return {
            "U": lambda: (x, y-1),
            "L": lambda: (x-1, y),
            "R": lambda: (x+1, y),
            "D": lambda: (x, y+1),
        }.get(move, lambda: print("This is a bug! Missing operation in dict"))()


def check_adjacents_squares(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            count += matrix[y+i][x+j]
            # print("matrix[%d][%d] = %d" % (y+i, x+j, matrix[y+i][x+j]))   
    return count

puzzle_input = 361257
limit = 1000    # since 1000**2 >> puzzle_input

x, y = int(limit/2), int(limit/2)
matrix = [ limit*[0] for _ in range(limit) ]

matrix[y][x] = 1
current_total = 1
corner = 1

while current_total < puzzle_input:
    move_list = ["R"] + (corner)*["U"] + (corner+1)*["L"] + (corner+1)*["D"] + (corner+1)*["R"]
    for move in move_list:
        new_x, new_y = process_move(move, x, y)
        matrix[new_y][new_x] = current_total = check_adjacents_squares(new_x, new_y)
        x, y = new_x, new_y
        
        # print(current_total, "matrix[%d][%d] = %d" % (new_y, new_x, matrix[new_y][new_x]))
        if current_total > puzzle_input:
            break
        print(current_total)
    corner += 2

print(current_total)
