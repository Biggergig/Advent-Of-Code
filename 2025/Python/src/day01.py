def main(input):
    p1 = p2 = 0

    pos = 50
    for line in input.splitlines():
        # parses input
        dist = int(line[1:])
        direction = -1 if line[0] == "L" else 1

        print(f"\nLINE: {line} (starting {pos=})")

        print(f"dist is {dist}, turns={dist//100}, remainder={dist%100}")
        full_rotations = dist // 100
        p2 += full_rotations
        if full_rotations:
            print(f"+{full_rotations} full rotations")
        dist %= 100

        if direction == -1 and pos == 0 and dist > 0:
            pos = 100  # don't count moving over

        pos += dist * direction
        if pos < 0 or pos > 100:
            p2 += 1
            print(f"+1 due to overshoot ({pos=})")
        pos %= 100

        if pos == 0:
            p1 += 1
            if not full_rotations:
                p2 += 1
                print("+1 because of ending at 0")
        print(f"after line: {p2=}")
    return p1, p2
