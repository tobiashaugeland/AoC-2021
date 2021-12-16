import igraph as ig
import numpy as np
FILE = "input.txt"
inp = []

with open(FILE, "r") as f:
    for l in f.readlines():
        inp.append([])
        for c in l.strip():
            inp[-1].append(int(c))


def create_graph(inp):
    rows = len(inp)
    cols = len(inp[0])
    vertices = rows*cols
    g = ig.Graph(vertices, directed=True)
    weights = []
    edges = []
    for i in range(vertices):
        y = i // rows
        x = i % cols

        if x > 0:
            edges.append((i, i-1))
            weights.append(inp[y][x-1])
        if x < cols-1:
            edges.append((i, i+1))
            weights.append(inp[y][x+1])
        if y > 0:
            edges.append((i, i-cols))
            weights.append(inp[y-1][x])
        if y < rows-1:
            edges.append((i, i+cols))
            weights.append(inp[y+1][x])

    g.add_edges(edges)
    g.es["weight"] = weights
    return g


def part1(inp):
    g = create_graph(inp)
    d = g.shortest_paths(0, g.vcount()-1, g.es["weight"])
    return int(d[0][0])


def part2(inp):
    rows = len(inp)
    grid_size = 5
    n = rows*grid_size
    grid = np.zeros((n, n), dtype=np.int16)
    for i in range(grid_size):
        rows = len(inp)
    cols = len(inp[0])
    grid_size = 5
    n = rows*grid_size
    grid = np.zeros((n, n), dtype=np.int16)

    for i in range(grid_size):
        for j in range(grid_size):
            for y in range(len(inp)):
                for x in range(len(inp[0])):
                    grid[y + i*rows][x + j * cols] = (inp[y][x] + i + j - 1) % 9 + 1
        for j in range(grid_size):
            for y in range(len(inp)):
                for x in range(len(inp[0])):
                    grid[y + i*rows][x + j * cols] = (inp[y][x] + i + j - 1) % 9 + 1

    g = create_graph(grid)
    d = g.shortest_paths(0, g.vcount()-1, g.es["weight"])
    return int(d[0][0])


print("Part 1:", part1(inp))
print("Part 2:", part2(inp))
