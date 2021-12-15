import numpy as np
FILE = "input.txt"
x_max = 0
y_max = 0

with open(FILE, "r") as f:
    x_set = set()
    y_set = set()
    for l in f.readlines():
        if "," in l:
            x, y = l.strip().split(",")
            x_set.add(int(x))
            y_set.add(int(y))
    x_max = max(x_set)
    y_max = max(y_set)


grid = np.zeros((y_max+1, x_max+1), dtype=np.int16)
folds = []

with open(FILE, "r") as f:
    for l in f.readlines():
        l = l.strip()
        if "," in l:
            x, y = l.split(",")
            x, y = int(x), int(y)
            grid[y][x] += 1

        elif "fold" in l:
            l = l.split("=")
            n = int(l[1])
            axis = l[0][-1]
            folds.append((axis, n))


def print_arr(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if arr[y][x] > 0:
                print("⬜", end="")
            else:
                print("⬛", end="")
        print()


def fold(arr, axis, coord):
    if axis == "x":
        for i in range(len(arr)):
            current_row = 2
            for j in range(coord-1, -1, -1):
                arr[i][j] += arr[i][j+current_row]
                current_row += 2
        arr = arr[:, :coord]

    elif axis == "y":
        current_row = 2
        for i in range(coord + 1, len(arr)):
            for j in range(len(arr[0])):
                arr[i-current_row][j] += arr[i][j]
            current_row += 2
        arr = arr[:coord, :]
    return arr


def part1(arr):
    axis = folds[0][0]
    n = folds[0][1]
    arr = fold(arr, axis, n)
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 0:
                count += 1
    return count


def part2(arr):
    for f in folds:
        arr = fold(arr, f[0], f[1])
    print_arr(arr)


print("Part 1:", part1(grid))
part2(grid)
