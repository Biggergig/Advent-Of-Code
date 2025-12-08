def main(input):
    p1 = p2 = 0
    start, *rest = input.splitlines()
    beams = {start.find("S")}
    (start_pos,) = beams
    splitters_rows = []
    for row in rest:
        splitters_rows.append({i for i, v in enumerate(row) if v == "^"})

    for splitters in splitters_rows:
        new_beams = beams - splitters  # all that didn't split
        for pos in beams & splitters:
            new_beams.add(pos - 1)
            new_beams.add(pos + 1)
            # print("split here")
            p1 += 1
        beams = new_beams
        # break

    # P2
    paths = [1] * len(start)
    for splitters in reversed(splitters_rows):
        new_paths = paths.copy()
        for sp in splitters:
            new_paths[sp] = paths[sp - 1] + paths[sp + 1]
        paths = new_paths
    p2 = paths[start_pos]
    return p1, p2
