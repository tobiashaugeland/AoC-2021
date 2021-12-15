from collections import defaultdict

neighbours = defaultdict(set)
discovered = set()

with open("input.txt", "r") as f:
    for l in f.readlines():
        a, b = l.strip().split("-")
        neighbours[a].add(b)
        neighbours[b].add(a)


def dfs_rec(u, discovered, can_twice):
    if u == "end":
        return 1
    paths = 0
    for v in neighbours[u]:
        if v.islower():
            if v not in discovered:
                paths += dfs_rec(v, discovered | {v}, can_twice)
            elif can_twice and v not in {"start", "end"}:
                paths += dfs_rec(v, discovered | {v}, False)
        else:
            paths += dfs_rec(v, discovered, can_twice)
    return paths


print("Part 1:", dfs_rec("start", {"start"}, False))
print("Part 2:", dfs_rec("start", {"start"}, True))
