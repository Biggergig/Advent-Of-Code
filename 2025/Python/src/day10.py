from collections import deque
from z3 import *

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

def solve_p2(switches, joltage):
    # print()
    # print(switches)
    # print(joltage)
    equations = joltage
    variables = [Int(f'b_{i}') for i in range(len(switches))]
    total_presses = Int("total_presses")
    for var, sw in zip(variables,switches):
        for i in sw:
            equations[i]-=var
    for i in range(len(equations)):
        equations[i] = (equations[i] == 0)

    s = Optimize()
    s.add(*equations, sum(variables) == total_presses, *(v>=0 for v in variables))
    s.minimize(total_presses)
    
    s.check()
    model = s.model()
    # print(model)
    return int(model[total_presses].as_long())


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
        p2 += solve_p2(switches_list, joltage_list)

    return p1, p2
