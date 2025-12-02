def is_invalid(inp, chunk_size):
    if len(inp) % chunk_size:
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
        for n in range(int(a), int(b) + 1):
            n = str(n)
            if len(n) % 2 == 0:  # even length
                if is_invalid(n, len(n) // 2):
                    p1 += int(n)
            for chunk_size in range(1, len(n) // 2 + 1):
                if is_invalid(n, chunk_size):
                    p2 += int(n)
                    break
    return p1, p2
