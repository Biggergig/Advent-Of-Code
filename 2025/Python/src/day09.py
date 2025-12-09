def main(input):
    p1 = p2 = 0
    points = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    print(points)

    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i + 1 :]:
            p1 = max((abs(y1 - y2) + 1) * (abs(x2 - x1) + 1), p1)

    # do they overlap?

    return p1, p2
