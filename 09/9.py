heightmap = []

with open("input.txt", "r") as f:
    for i, l in enumerate(f.readlines()):
        heightmap.append([])
        for c in l.strip():
            heightmap[i].append(int(c))


def find_low_points(heightmap):
    h = heightmap
    x_max = len(h[0])
    y_max = len(h)

    low_points = []
    for y in range(y_max):
        for x in range(x_max):
            horizontal_lower = False
            vertical_lower = False
            point = h[y][x]
            if x > 0 and x < x_max-1:
                horizontal_lower = point < h[y][x+1] and point < h[y][x-1]
            elif x == 0:
                horizontal_lower = point < h[y][x+1]
            else:
                horizontal_lower = point < h[y][x-1]

            if y > 0 and y < y_max-1:
                vertical_lower = point < h[y+1][x] and point < h[y-1][x]
            elif y == 0:
                vertical_lower = point < h[y+1][x]
            else:
                vertical_lower = point < h[y-1][x]
            if horizontal_lower and vertical_lower:
                low_points.append((x, y))
    return low_points


def calculate_risk(heightmap):
    low_points = find_low_points(heightmap)
    risk = 0
    for point in low_points:
        risk += 1 + heightmap[point[1]][point[0]]
    return risk


print("Part 1:", calculate_risk(heightmap))


def find_basins(heightmap):
    low_points = find_low_points(heightmap)
    h = heightmap
    x_max = len(h[0])
    y_max = len(h)
    basins = []
    for low_point in low_points:
        in_basin = {low_point}
        working_pool = [low_point]
        while len(working_pool) > 0:
            for point in working_pool:
                x = point[0]
                y = point[1]
                val = h[y][x]
                # check left side
                if x > 0:
                    if val < h[y][x-1] and h[y][x-1] < 9:
                        working_pool.append((x-1, y))
                # right
                if x < x_max-1:
                    if val < h[y][x+1] and h[y][x+1] < 9:
                        working_pool.append((x+1, y))
                # top
                if y > 0:
                    if val < h[y-1][x] and h[y-1][x] < 9:
                        working_pool.append((x, y-1))
                # bottom
                if y < y_max-1:
                    if val < h[y+1][x] and h[y+1][x] < 9:
                        working_pool.append((x, y+1))
                in_basin = in_basin.union(set(working_pool))
                working_pool.remove(point)
        basins.append(in_basin)
    return(basins)


def solve_part2(heightmap):
    basins = sorted(find_basins(heightmap), key=len)
    total = 1
    for i in range(3):
        total *= len(basins[~i])
    return total


print("Part 2:", solve_part2(heightmap))
