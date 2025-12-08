from heapq import *
from collections import Counter


def get_dist(p1, p2):
    return sum((b - a) ** 2 for a, b in zip(p1, p2)) ** 0.5


class DisjointSet:
    def __init__(self, size):
        self.rep = list(range(size))

    def get_rep(self, pos):
        if self.rep[pos] != pos:
            self.rep[pos] = self.get_rep(self.rep[pos])
        return self.rep[pos]

    def join(self, a, b):
        r = self.get_rep(a)
        self.rep[r] = self.get_rep(b)

    def n_groups(self):
        self.consolidate()
        return len(set(self.get_rep(i) for i in range(len(self.rep))))

    def consolidate(self):
        for i in range(len(self.rep)):
            self.get_rep(i)

    def __repr__(self):
        return self.rep.__repr__()


def main(input):
    if len(input.splitlines()) > 100:
        p1_iters = 1000
    else:
        p1_iters = 10
    p1 = p2 = 0
    points = [tuple(map(int, line.split(","))) for line in input.splitlines()]
    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append((get_dist(points[i], points[j]), i, j))
    heapify(distances)

    DS = DisjointSet(len(points))
    for i in range(p1_iters):
        dist, a, b = heappop(distances)
        DS.join(a, b)
    DS.consolidate()
    p1 = 1
    for _, sz in Counter(DS.rep).most_common(3):
        p1 *= sz
    for _ in range(DS.n_groups() - 1):
        while True:
            dist, a, b = heappop(distances)
            if DS.get_rep(a) != DS.get_rep(b):
                break
        DS.join(a, b)
        p2 = points[a][0] * points[b][0]

    return p1, p2
