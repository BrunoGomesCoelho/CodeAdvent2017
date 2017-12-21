"""
The resolution bases itself on the fact that given a number X:
-- First find out the highest odd numbers "corner" such that corner**2 <= X
That is, a number that is in the diagonal that connects 1 to 9 to 25 to 49....
-- Then we know that the move list so far will be:
    R 1U 2L 2D 2R
    R 3U 4L 4D 4R
    R 5U 6L 6D 6R
    ....
    .
    .
    R (corner-2)*U  (corner-1)*L  (corner-1)*D  (corner-1)*R

We can see that after a full cycle, we have 1R + 1U
so after cicles = corner // 2, we would have cicles*(1R + 1U) moves.

then find how many steps are missing from our original number
(X - corner**2) and go through our move list moving as needed, making sure to
cancel a L with a R/U with a D and vice-versa.
"""


from math import sqrt



def process_move(move, u, l, r, d):
    return {
            "U": lambda: (u+1, l, r, d) if d == 0 else (u, l, r, d-1),
            "L": lambda: (u, l+1, r, d) if r == 0 else (u, l, r-1, d),
            "R": lambda: (u, l, r+1, d) if l == 0 else (u, l-1, r, d),
            "D": lambda: (u, l, r, d+1) if u == 0 else (u-1, l, r, d),
        }.get(move, lambda: print("This is a bug! Missing operation in dict"))()


# Our input
# x = 1024
x = 361527

corner = int(sqrt(x))

if corner % 2 == 0:
    corner -= 1
cicles = corner // 2


# counts for each direction
u = l = 0
r = d = cicles

move_list = ["R"] + (corner)*["U"] + (corner+1)*["L"] + (corner+1)*["D"] + (corner+1)*["R"]


for move in move_list[0: (x-corner**2)]:
    u, l, r, d = process_move(move, u, l, r, d)

print(u + l + r + d)

