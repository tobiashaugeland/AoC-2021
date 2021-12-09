inp = []
with open("input.txt", "r") as f:
    l = f.readline().strip().split(",")
    inp = [int(x) for x in l]

hi = max(inp)
lo = min(inp)

# brute force all positions
def part1(inp):
    cheapest = float("inf")
    pos = 0
    for i in range(lo, hi+1):
        total = 0
        for j in range(len(inp)):
            total += abs(inp[j]-i)
        if total < cheapest:
            cheapest = total
            pos = i
    return cheapest, pos


print("Part 1:", part1(inp)[0])

# brute force all positions
def part2(inp):
    cheapest = float("inf")
    pos = 0
    for i in range(lo, hi+1):
        total = 0
        for j in range(len(inp)):
            n = abs(inp[j]-i)
            # sum of n first integers: n*(n+1)/2
            total += int(n*(n+1)/2)
        if total < cheapest:
            cheapest = total
            pos = i
    return cheapest, pos


print("Part 2:", part2(inp)[0])
