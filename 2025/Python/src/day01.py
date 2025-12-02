def main(input):
    p1 = p2 = 0

    pos = 50
    for line in input.splitlines():
        # parses input
        dist = int(line[1:])
        direction = -1 if line[0] == "L" else 1
        dist *= direction

        # make turns
        pos += dist

        # part 2
        if pos == 0:  # record if we ended at 0 (not 100)
            p2 += 1
        p2 += abs(pos // 100)
        if pos == dist and pos < 0:  # if didn't start at 0
            p2 -= 1

        print(line, pos % 100, pos, pos // 100, p2, sep="\t")
        pos %= 100

        # part 1 - check if we end at 0
        if pos == 0:
            p1 += 1

    return p1, p2
