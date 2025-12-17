from collections import deque
def main(input):
    p1 = p2 = 0

    nodes = {'out':[]}
    paths = {'out':0}
    for line in input.splitlines():
        n, *out = line.split()
        n = n[:-1]
        nodes[n] = out
        paths[n] = 0
    paths['you'] = 1

    done = set()
    q = deque(['you'])
    while q:
        n = q.popleft()
        if n in done: continue
        done.add(n)
        for e in nodes[n]:
            paths[e]+=paths[n]
            q.append(e)
    print(paths)

    print(nodes)
    p1 = paths['out']

    return p1, p2
