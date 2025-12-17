from collections import Counter
def main(input):
    p1 = p2 = 0
    *raw_pieces, lines = input.split('\n\n')
    pieces = [raw.count('#') for raw in raw_pieces]
    print(pieces)
    C = Counter()
    for line in lines.splitlines():
        print(line,end='\t')
        lhs,rhs = line.split(':')
        w,h = map(int,lhs.split('x'))
        C[(w,h)]+=1
        counts = list(map(int, rhs.split()))
        if (w*h - sum(a*b for a,b in zip(pieces, counts)))<0:
            print('X - impossible')
            continue
        p1+=1
        print()

    return p1, p2
