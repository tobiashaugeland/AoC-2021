FILE = "input.txt"

rules = {}
template = ""


with open(FILE, "r") as f:
    for l in f.readlines():
        l = l.strip()
        if "->" in l:
            l = l.split("->")
            rules[l[0].strip()] = l[1].strip()
        elif l.isalpha():
            template = l

uniques = set(rules.values())


def naive_step(tem):
    to_add = []
    for i in range(len(tem)):
        key = tem[i:i+2]
        if key in rules.keys():
            to_add.append((rules[key], i+1))
    for i, elem in enumerate(to_add):
        c = elem[0]
        index = elem[1]
        tem = tem[:index+i] + c + tem[index+i:]
    return tem


def naive_solve(tem, iterations):
    for i in range(iterations):
        tem = naive_step(tem)
    hi = float("-inf")
    lo = float("inf")
    for c in uniques:
        n = tem.count(c)
        if n > hi:
            hi = n
        if n < lo:
            lo = n
    return hi-lo


def create_empty_count():
    count = {}
    for r in rules:
        count[r] = 0
    return count


def get_count(tem):
    count = create_empty_count()
    for i in range(len(tem)-1):
        key = tem[i:i+2]
        count[key] += 1
    return count


def smart_step(count):
    temp_count = create_empty_count()
    for key in count:
        n = count[key]
        if n > 0:
            r = rules[key]
            key_1 = key[0]+r
            key_2 = r + key[1]

            temp_count[key] -= n
            temp_count[key_1] += n
            temp_count[key_2] += n
    for key in temp_count:
        count[key] += temp_count[key]
    return count


def smart_solve(tem, iterations):
    last_char = tem[-1]
    count = get_count(tem)
    for i in range(iterations):
        count = smart_step(count)

    unique_counter = {}
    for u in uniques:
        unique_counter[u] = 0

    # counts up all unique chars, will be 1 off on the last char
    for key in count:
        unique_counter[key[0]] += count[key]
    unique_counter[last_char] += 1

    val = unique_counter.values()
    diff = max(val) - min(val)

    return diff


print("Part 1:", naive_solve(template, 10))
print("Part 2:", smart_solve(template, 40))
