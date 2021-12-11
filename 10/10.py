from math import floor
points1 = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

points2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

data = []
with open("input.txt", "r") as f:
    for l in f.readlines():
        data.append(l.strip())


# returns score if line is corrupted, if not it returns 0
def is_corrupted(line):
    openers = "([{<"
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    stack = []
    for c in line:
        if c in openers:
            stack.append(pairs[c])
        else:
            top = stack.pop()
            if not c == top:
                return points1[c]
    return 0


def part1(data):
    score = 0
    for l in data:
        score += is_corrupted(l)
    return score


def complete_line(line):
    openers = "([{<"
    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score = 0
    stack = []
    for c in line:
        if c in openers:
            stack.append(pairs[c])
        else:
            stack.pop()
    while len(stack) > 0:
        top = stack.pop()
        score *= 5
        score += points2[top]
    return score


def part2(data):
    scores = []
    for l in data:
        if not is_corrupted(l):
            scores.append(complete_line(l))
    scores.sort()
    return scores[floor(len(scores)/2)]


print("Part 1: ", part1(data))
print("Part 2: ", part2(data))
