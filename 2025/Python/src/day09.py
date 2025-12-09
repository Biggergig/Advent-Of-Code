def intersect(rect, line):
    (x1, y1), (x2, y2) = rect
    (a1, a2), (b1, b2) = line
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    assert a1 <= a2 and b1 <= b2

    if (a1, b1) in rect or (a2, b2) in rect:

        return False
    if a2 < x1 or x2 < a1:
        # X is not overlapping
        # print("x is not overlapping", (x1, x2), (a1, a2))
        return False
    if b2 < y1 or y2 < b1:
        # Y is not overlapping
        # print("y is not overlapping", line)
        return False
    # print(rect, line, "overlap!")
    return True


def main(input):
    part1 = part2 = 0
    points = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    # print(points)

    lines = []

    for p1, p2 in zip(points, points[1:] + points[:1]):
        lines.append((sorted([p1[0], p2[0]]), sorted([p1[1], p2[1]])))
    # print(lines)

    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i + 1 :]:
            # if not ((x2, y2) == (2, 3) and (x1, y1) == (11, 7)):
            #     continue
            if not any(intersect(((x1, y1), (x2, y2)), line) for line in lines):
                # print(
                #     (x1, y1),
                #     (x2, y2),
                #     "is valid for p2",
                #     (abs(y1 - y2) + 1) * (abs(x2 - x1) + 1),
                # )
                part2 = max((abs(y1 - y2) + 1) * (abs(x2 - x1) + 1), part2)
            part1 = max((abs(y1 - y2) + 1) * (abs(x2 - x1) + 1), part1)

    # do they overlap?
    # import matplotlib.pyplot as plt
    # from matplotlib.patches import Polygon

    # for i in range(len(points)):
    #     print(points[i - 1], points[i])
    #     plt.plot(points[i - 1], points[i])
    # fig, ax = plt.subplots()
    # polygon = Polygon(
    #     points, closed=True, facecolor="green", edgecolor="black", linewidth=2
    # )
    # ax.add_patch(polygon)
    # ax.set_ylim(00000, 100000)
    # ax.set_xlim(00000, 100000)
    # ax.set_aspect("equal", adjustable="box")  # Ensures the square appears as a square
    # plt.title("Square using Polygon patch")
    # plt.xlabel("X-axis")
    # plt.ylabel("Y-axis")
    # plt.grid(True)

    # plt.show()
    return part1, part2
