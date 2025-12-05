def main(input):
    p1 = p2 = 0
    ranges, ingredients = input.split("\n\n")
    ranges = [tuple(map(int, l.split("-"))) for l in ranges.splitlines()]
    ingredients = list(map(int, ingredients.splitlines()))

    for i in ingredients:
        for l, h in ranges:
            if l <= i <= h:
                p1 += 1
                break

    ranges.sort()
    l, r = ranges[0]
    for a, b in ranges:
        if l <= a <= r:
            r = max(b, r)
        else:
            p2 += r - l + 1
            l = a
            r = b
    p2 += r - l + 1

    return p1, p2
