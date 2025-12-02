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
        print(line, pos)

        while pos < 0:
            p2 += 1
            pos += 100
            print("click!", p2, pos, sep="\t")

        while pos > 99:
            p2 += 1
            pos -= 100
            print("click!", p2, pos, sep="\t")
        print("line done, p2 =", p2)

        # part 1 - check if we end at 0
        if pos == 0:
            p1 += 1

    return p1, p2
