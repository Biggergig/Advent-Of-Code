def is_invalid(inp, chunk_size):
    if chunk_size == 0 or len(inp) % chunk_size:
        return False
    for i in range(chunk_size):
        tmp = {c for c in inp[i::chunk_size]}
        # print(inp, i, chunk_size, tmp)
        if len(tmp) != 1:
            return False
    return True


def main(input):
    p1 = p2 = 0
    for pair in input.split(","):
        a, b = pair.split("-")
        print(a, b)
        for n in range(int(a), int(b) + 1):
            n = str(n)
            if is_invalid(n, len(n) // 2):
                p1 += int(n)
                print("!!!", n)
    return p1, p2
