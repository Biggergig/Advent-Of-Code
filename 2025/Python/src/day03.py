def get_joltage(line):
    DP = ['']+[None]*12
    for c in reversed(line):
        for i in range(12,0,-1):
            if DP[i-1] is not None:
                DP[i]=max(DP[i] or -1,int(c + str(DP[i-1])))
    return DP[2],DP[12]

def main(input):
    p1 = p2 = 0
    for line in input.splitlines():
        a,b = get_joltage(line)
        p1+=a
        p2+=b
    return p1, p2
