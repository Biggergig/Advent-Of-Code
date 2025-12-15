from collections import deque


class State:
    def __init__(self, lights, switches, dist=0):
        self.lights = lights
        self.switches = switches
        self.dist = dist

    def next_states(self):
        for sw in self.switches:
            yield State(self.lights ^ sw, self.switches, self.dist + 1)


def solve_p1(start_state):
    q = deque([start_state])
    seen = set()
    while True:
        s = q.popleft()
        if s.lights in seen:
            continue
        seen.add(s.lights)
        if s.lights == 0:
            return s.dist
        for ns in s.next_states():
            if ns not in seen:
                q.append(ns)
        # print(q)


def main(input):
    p1 = p2 = 0

    for line in input.splitlines():
        lights, *switches, joltage = line.split()
        lights = int(lights[1:-1][::-1].replace(".", "0").replace("#", "1"), 2)
        switches_num = []
        for switch in switches:
            val = 0
            for v in map(int, switch[1:-1].split(",")):
                val += 1 << v
            switches_num.append(val)
        start = State(lights, switches_num)
        p1 += solve_p1(start)
        print(line, p1)
    return p1, p2
