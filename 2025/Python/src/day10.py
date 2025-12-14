class State:
    def __init__(self, lights, switches, dist=0):
        self.lights = lights
        self.switches = switches
        self.dist = dist


def main(input):
    p1 = p2 = 0

    for line in input.splitlines():
        lights, *switches, joltage = line.split()
        lights = int(lights[1:-1][::-1].replace(".", "0").replace("#", "1"), 2)
        for switch in switches:
            print(switch)
        start = State(lights, None)
        print(lights)
    return p1, p2
