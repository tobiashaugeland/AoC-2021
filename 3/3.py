data = [s.strip() for s in open("input.txt", "r").readlines()]

def part1(data):
    gamma = ""

    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for j in range(len(data)):
            if data[j][i] == "0":
                zeroes += 1
            else:
                ones += 1
        if zeroes > ones:
            gamma += "0"
        else:
            gamma += "1"

    n = len(gamma)
    gamma = int(gamma, 2)
    epsilon = gamma ^ int(b'1'*n, 2)
    return gamma*epsilon

# get o2 or co2 rating
def part2(data, rating="o2"):
    bits = []
    if rating =="o2":
        bits =["1","0"]
    elif rating == "co2":
        bits=["0","1"]
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        for j in range(len(data)):
            if data[j][i] == "0":
                zeroes += 1
            else:
                ones += 1
        if ones >= zeroes:
            data = [x for x in data if x[i] == bits[0]]
        else:
            data = [x for x in data if x[i] == bits[1]]
        if len(data) == 1:
            return int(data[0],2)

print("Part 1:",part1(data))
print("Part 2:",part2(data, "o2")* part2(data, "co2"))
