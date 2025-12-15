from collections import deque, Counter


class State:
    def __init__(self, lights, switches, dist=0):
        self.lights = lights
        self.switches = switches
        self.dist = dist

    def next_states(self):
        for sw in self.switches:
            yield State(self.lights ^ sw, self.switches, self.dist + 1)


class State_2:
    def __init__(self, switches, joltage, dist=0, lights=None, target=None):
        if lights is None:
            self.lights = Counter()
        else:
            self.lights = lights
        self.switches = switches
        if target is None:
            self.target = Counter(dict(zip(range(len(joltage)), joltage)))
        else:
            self.target = target
        # print(self.lights, self.switches)
        # print(self.target)
        self.dist = dist

    def next_states(self):
        for sw in self.switches:
            new_lights = self.lights + sw
            if len(new_lights - self.target) != 0:
                continue
            yield State_2(self.switches, None, self.dist + 1, new_lights, self.target)


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


def _hash_counter(c):
    return tuple(sorted(c.items()))


def solve_p2(start_state):
    q = deque([start_state])
    seen = set()
    while True:
        s = q.popleft()
        if _hash_counter(s.lights) in seen:
            continue
        seen.add(_hash_counter(s.lights))
        if s.lights == s.target:
            return s.dist
        for ns in s.next_states():
            if ns not in seen:
                q.append(ns)


def _text_to_list(text):
    return list(map(int, text[1:-1].split(",")))


def main(input):
    p1 = p2 = 0

    for line in input.splitlines():
        lights, *switches, joltage = line.split()
        lights = int(lights[1:-1][::-1].replace(".", "0").replace("#", "1"), 2)
        switches_num = []
        for switch in switches:
            val = 0
            for v in map(int, _text_to_list(switch)):
                val += 1 << v
            switches_num.append(val)
        start = State(lights, switches_num)
        p1 += solve_p1(start)

        sw_2 = []
        for sw in switches:
            c = Counter()
            for s in _text_to_list(sw):
                c[s] += 1
            sw_2.append(c)
        s2 = State_2(sw_2, _text_to_list(joltage), 0)
        p2 += solve_p2(s2)

    return p1, p2
