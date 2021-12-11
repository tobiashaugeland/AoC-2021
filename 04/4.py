f = open("input.txt", "r")

draws = [int(x) for x in f.readline().strip().split(",")]

boards = []

board_index = 0
for l in f.readlines():
    if l == "\n":
        boards.append([])
    else:
        boards[-1].append([int(x) for x in l.strip().split(" ") if x != ""])

# check if a board with 'x' or '' has a bingo
def check_board(marked):
    for i in range(len(marked)):
        x = [x for x in marked[i] if x == "x"]
        if len(x) == 5:
            return True
    for i in range(len(marked)):
        x = []
        for j in range(len(marked[i])):
            if marked[j][i] == "x":
                x.append("x")
        if len(x) == 5:
            return True
    return False

# compute score of a board
# (sum of all unmarked numbers) * (last number called)
def get_score(board, marked, num):
    total = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if marked[i][j] != "x":
                total += board[i][j]
    return total*num

def solve(boards):
    best = []
    best_marked = []
    lowest_turn = float("inf")
    best_num = 0
    worst = []
    worst_marked = []
    highest_turn = 0
    worst_num = 0
    for board in boards:
        marked = []
        for i in range(len(board)):
            marked.append(["","","","",""])
        for turn, num in enumerate(draws):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == num:
                        marked[i][j] = "x"
            if check_board(marked):
                if turn < lowest_turn:
                    lowest_turn = turn
                    best = board
                    best_marked = marked
                    best_num = num
                if turn > highest_turn:
                    highest_turn = turn
                    worst = board
                    worst_marked = marked
                    worst_num = num
                break
                    
    part1 = get_score(best, best_marked, best_num)
    part2 = get_score(worst, worst_marked, worst_num)
    return part1, part2

solution = solve(boards)

print("Part 1:", solution[0])
print("Part 2:", solution[1])