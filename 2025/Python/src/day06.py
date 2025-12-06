def part1(nums, sym):
    if sym == "*":
        ans = 1
        for n in nums:
            ans *= n
    else:
        ans = 0
        for n in nums:
            ans += n
    return ans


def main(input):
    p1 = p2 = 0
    *nums_list, sym_list = map(lambda x: x.split(), input.splitlines())
    nums_list = [list(map(int, x)) for x in zip(*nums_list)]

    for nums, sym in zip(nums_list, sym_list):
        p1 += part1(nums, sym)

    p2_input = [*zip(*(input + " " * 5).splitlines())]
    i = 0

    while i < len(p2_input):
        *num, sym = p2_input[i]
        ans = int("".join(num))
        i += 1
        while i < len(p2_input) and set(p2_input[i]) != {
            " ",
        }:
            tmp = int("".join(p2_input[i]))
            if sym == "*":
                ans *= tmp
            else:
                ans += tmp
            i += 1
        i += 1
        p2 += ans

    return p1, p2
