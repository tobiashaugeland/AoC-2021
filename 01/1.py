data = [int(l.strip()) for l in open("input.txt", "r").readlines()]

def get_increasing(data):
    counter = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            counter += 1
    return counter

print(get_increasing(data))

def get_increasing_window(data):
    counter = 0
    for i in range(2, len(data)-1):
        w_1 = data[i] + data[i-1] + data[i-2]
        w_2 = data[i+1] + data[i] + data[i-1]
        if w_2 > w_1:
            counter += 1
    return counter

print(get_increasing_window(data))
