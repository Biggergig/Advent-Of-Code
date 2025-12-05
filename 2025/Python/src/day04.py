def get_adj(p):
    return {p+1,p-1,p+1j,p-1j,p+1+1j,p+1-1j,p-1+1j,p-1-1j}

def clean(grid):
    removed = 0
    remaining = set()

    for p in grid:
        if len(grid & get_adj(p)) < 4:
            removed+=1
        else:
            remaining.add(p)

    return remaining, removed

def main(input):
    p1 = p2 = 0
    grid = set()
    for y, row in enumerate(input.splitlines()):
        for x,v in enumerate(row):
            if v == '@':
                grid.add(x + y*1j)
    
    ng, p1 = clean(grid)
    rem = p1
    while rem:
        p2+=rem
        ng, rem = clean(ng)
    return p1, p2
