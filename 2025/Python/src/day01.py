def main(input):
    p1 = p2 = 0

    pos = 50
    for line in input.splitlines():
        # parses input
        dist = int(line[1:])
        direction = -1 if line[0] == "L" else 1
        for _ in range(dist):
            pos += direction
            pos %= 100
            if pos == 0:
                p2 += 1
        if pos == 0:
            p1 += 1
    return p1, p2
