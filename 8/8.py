from itertools import permutations

"""
antall: 2, 3, 4, 5, 5, 5, 6, 6, 6, 7
tall  : 1, 7, 4, 5, 2, 3, 0, 6, 9, 8
"""

inp = []

with open("input.txt", "r") as f:
    for l in f.readlines():
        l = l.split("|")
        left = [x for x in l[0].strip().split(" ")]
        right = [x for x in l[1].strip().split((" "))]
        inp.append((left, right))


def find_1_4_7(inp):
    total = 0
    for l in inp:
        for seq in l[1]:
            n = len(seq)
            if n in [2, 3, 4, 7]:
                total += 1
    return total


print("Part 1:",find_1_4_7(inp))

# dict which string maps to which number with a given key
def get_solutions(k):
    sol = {
        "".join(sorted([k[0], k[1], k[2], k[4], k[5], k[6]])): 0,
        "".join(sorted([k[2], k[5]])): 1,
        "".join(sorted([k[0], k[2], k[3], k[4], k[6]])): 2,
        "".join(sorted([k[0], k[2], k[3], k[5], k[6]])): 3,
        "".join(sorted([k[1], k[2], k[3], k[5]])): 4,
        "".join(sorted([k[0], k[1], k[3], k[5], k[6]])): 5,
        "".join(sorted([k[0], k[1], k[3], k[4], k[5], k[6]])): 6,
        "".join(sorted([k[0], k[2], k[5]])): 7,
        "".join(sorted([k[0], k[1], k[2], k[3], k[4], k[5], k[6]])): 8,
        "".join(sorted([k[0], k[1], k[2], k[3], k[5], k[6]])): 9,
    }
    return sol

# check if a key solves all the scrambled digits
def is_correct(digits, key):
    sols = get_solutions(key)
    digits = set(["".join(sorted(x)) for x in digits])
    keys = set(sols.keys())
    return keys == digits

# returns the number based on scrambled input and a given key
def decode(digits, key):
    out = ""
    sols = get_solutions(key)
    for d in digits:
        out += str(sols["".join(sorted(d))])
    return int(out)

# brute force solution to a given line
def decode_output(line):
    chars = "abcdefg"
    perms = permutations(chars)
    digits = line[0]
    outs = line[1]
    for p in perms:
        if is_correct(digits, p):
            return decode(outs, p)

# decode the output of all the lines, and sum it up
def find_all(inp):
    total = 0
    for line in inp:
        total += decode_output(line)
    return total

print("Part 2:",find_all(inp))