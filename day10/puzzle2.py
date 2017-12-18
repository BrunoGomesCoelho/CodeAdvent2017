def knot_hash(line):

    size = 256

    line = [ord(x) for x in line] + [17, 31, 73, 47, 23]

    lst = [x for x in range(size)]

    skip_size = 0
    pos = 0

    # Hashes
    for _ in range(64):
        for lenght in line:
            end = (pos - 1 + lenght) % size
            for i in range(0, lenght // 2):
                lst[(pos + i) % size], lst[(end - i) % size] = \
                    lst[(end - i) % size], lst[(pos + i) % size]
            pos = (lenght + skip_size + pos) % size
            skip_size += 1

    # Performs the xor operation from sparse to dense hash 

    ans = []
    for i in range(16):
        temp = lst[i*16]
        for j in range(1, 16):
            temp ^= lst[i*16 + j]
        ans.append(temp)
    
    return ans

if __name__ == "__main__":
    line = input()
    ans = knot_hash(line)
    txt = ""
    for num in ans:
        txt += format(num, "02x")
    print(txt)

