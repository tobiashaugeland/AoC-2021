inp = []

with open("input.txt", "r") as f:
    for l in f.readlines():
        l = l.strip()
        pairs = l.split(" -> ")
        p1 = [int(x) for x in pairs[0].split(",")]
        p2 = [int(x) for x in pairs[1].split(",")]
        inp.append([p1, p2])

# should probably refactor this a bit :)
def generate_grid(inp, include_diag=False):
    grid = []

    for i in range(1000):
        grid.append([])
        for j in range(1000):
            grid[i].append(0)

    for l in inp:
        x1 = l[0][0]
        y1 = l[0][1]
        x2 = l[1][0]
        y2 = l[1][1]

        if x1 == x2:
            if y1 < y2:
                for y in range(y1, y2+1):
                    grid[y][x1] += 1
            else:
                for y in range(y2, y1+1):
                    grid[y][x1] += 1
        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2+1):
                    grid[y1][x] += 1
            else:
                for x in range(x2, x1+1):
                    grid[y1][x] += 1
        elif include_diag and abs(x2 - x1) == abs(y2-y1):
            x_cords = []
            y_cords = []
            if x2 > x1:
                x_cords = list(range(x1, x2+1))
            else:
                x_cords = list(range(x1, x2-1, -1))
            if y2 > y1:
                y_cords = list(range(y1, y2+1))
            else:
                y_cords = list(range(y1, y2-1, -1))
            for i in range(len(x_cords)):
                grid[y_cords[i]][x_cords[i]] += 1
    return grid


no_diag = generate_grid(inp, False)
with_diag = generate_grid(inp, True)


def get_overlapping_count(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 1:
                total += 1
    return total


print("Part 1:", get_overlapping_count(no_diag))
print("Part 2:", get_overlapping_count(with_diag))
