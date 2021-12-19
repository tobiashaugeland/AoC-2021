# target area: x=48..70, y=-189..-148
# to find x velocity, find the smallest integer
# where n(n+1)/2 >= 48
# n = 10 gives n(n+1)/2 = 55
# then bruteforce y values, starting low, increase until it overshoots

x_lo = 48
x_hi = 70

y_lo = -189
y_hi = -148


def is_inside(x,y):
    return x <= x_hi and x >= x_lo and y >= y_lo and y <= y_hi

def has_passed(x,y):
    return x > x_hi or y < y_lo

def is_valid(x_velocity, y_velocity):
    x_pos = 0
    y_pos = 0
    is_valid = True
    while True:
        x_pos += x_velocity
        y_pos += y_velocity

        if is_inside(x_pos, y_pos):
            break
        if has_passed(x_pos, y_pos):
            is_valid = False
            break

        if x_velocity > 0:
            x_velocity -= 1
        y_velocity -= 1
    return is_valid


def find_highest_velocity():
    best_y = 0
    for i in range(1,1000):
        x_velocity = 10
        y_velocity = i
        initial_y_velocity = i

        if is_valid(x_velocity, y_velocity):
            best_y = initial_y_velocity
    return best_y

def get_highest_point(y_velocity):
    y_pos = 0
    last_y = 0
    while True:
        y_pos += y_velocity
        y_velocity -= 1
        if y_pos <= last_y:
            break
        last_y = y_pos
    return y_pos


def unique_velocities():
    counter = 0
    for x in range(1, 80):
        for y in range(-200, 400):    
            if is_valid(x,y):
                counter += 1
    return counter

print("Part 1:",get_highest_point(find_highest_velocity()))
print("Part 2:",unique_velocities())

    