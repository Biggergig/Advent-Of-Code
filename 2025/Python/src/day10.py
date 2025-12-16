from collections import deque
from dataclasses import dataclass, field
from heapq import *

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


@dataclass
class State2:
    remaining: list
    presses: int
    h: int = field(init=False)
    dist: int = field(init=False)

    def __post_init__(self):
        self.h = max(self.remaining)
        self.dist = self.h + self.presses

    def is_valid(self):
        return all(v >= 0 for v in self.remaining)
    
    def __lt__(self, other):
        return self.dist<other.dist

def solve_p2(start_state, switches):
    switches.sort(key=len, reverse=True)
    print(start_state)
    print(switches)
    heap = [start_state]
    seen = set()
    while heap:
        st = heappop(heap)
        if tuple(st.remaining) in seen: continue
        seen.add(tuple(st.remaining))
        # print(st)
        if st.h == 0:
            return st.presses
        for sw in switches:
            tmp = st.remaining.copy()
            extra_presses = 0
            while True:
                extra_presses += 1
                for i in sw:
                    tmp[i]-=1
                new_state = State2(tmp.copy(), st.presses+extra_presses)
                if new_state.is_valid() and tuple(new_state.remaining) not in seen:
                    heappush(heap, new_state)
                else:
                    break
    assert False, "THIS SHOULD NEVER HIT"

def main(input):
    p1 = p2 = 0

    def _text_to_list(text):
        return list(map(int, text[1:-1].split(",")))

    for line in input.splitlines():
        lights, *switches, joltage = line.split()
        lights = int(lights[1:-1][::-1].replace(".", "0").replace("#", "1"), 2)
        switches_num = []
        for switch in switches:
            val = 0
            for v in _text_to_list(switch):
                val += 1 << v
            switches_num.append(val)
        start = State(lights, switches_num)
        p1 += solve_p1(start)

        joltage_list = _text_to_list(joltage)
        switches_list = list(map(_text_to_list,switches))
        s2 = State2(joltage_list, 0)
        p2 += solve_p2(s2, switches_list)


    return p1, p2
