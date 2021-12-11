import numpy as np
STEPS = 100

data = []

with open("input.txt", "r") as f:
    for i, l in enumerate(f.readlines()):
        data.append([])
        for c in l.strip():
            data[i].append(int(c))

data = np.array(data)
data = np.pad(data, [(1, 1), (1, 1)], mode="constant")



def step(data):
    has_flashed = np.zeros((len(data), len(data)), dtype=np.int16)
    flashes = 0
    # increment all by one
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            data[i][j] += 1

    while np.amax(data) > 9:
        for i in range(1, len(data)-1):
            for j in range(1, len(data[0])-1):
                val = data[i][j]
                if val > 9 and has_flashed[i][j] < 1:
                    flashes += 1
                    has_flashed[i][j] = 1
                    data[i][j] = 0
                    for y in range(i-1, i+2):
                        for x in range(j-1, j+2):
                            if x != j or y != i:
                                data[y][x] += 1

    # reset flashed points and padding
    for i in range(len(has_flashed)):
        for j in range(len(has_flashed[0])):
            if i == 0 or i == len(data)-1 or j == 0 or j == len(data)-1:
                data[i][j] = 0
            if has_flashed[i][j] > 0:
                data[i][j] = 0
    return data, flashes

def part1(inp):
    data = inp.copy()
    total_flashes = 0
    for _ in range(STEPS):
        data, flashes = step(data)
        total_flashes += flashes
    return total_flashes

def part2(inp):
    data = inp.copy()
    current_step = 0
    while True:
        current_step += 1
        data, flashes = step(data)
        if flashes == 100:
            return current_step

print(part1(data))
print(part2(data))