def get_joltage(line):
    largest = best = float('-inf')

    for c in map(int,reversed(line)):
        best = max(best,c*10 + largest)
        largest = max(largest, c)

    return best

def main(input):
    p2 = 0

    p1 = sum(get_joltage(line) for line in input.splitlines())

    return p1, p2
