fish = []

with open("input.txt", "r") as f:
    nums = f.readline().strip().split(",")
    for num in nums:
        fish.append(int(num))

# calculate fish with simulation
# too slow for part 2
def fish_sim(fish, days):
    fish = fish.copy()
    for _ in range(days):
        for i in range(len(fish)):
            if fish[i] == 0:
                fish.append(8)
                fish[i] = 6
            else:
                fish[i] -= 1
    return len(fish)

# calculate fish using a list of 9 numbers 
# representing amount of fish on each day
def fish_no_sim(fish, days):
    day_list = [0,0,0,0,0,0,0,0,0]
    for f in fish:
        day_list[f] += 1
    for _ in range(days):
        zeros = day_list.pop(0)
        day_list[6] += zeros
        day_list.append(zeros)
    return sum(day_list)

print("Part 1:",fish_sim(fish, 80))
print("Part 2:",fish_no_sim(fish, 256))