import math
import socket
import numpy as np

MAZE_SIZE = 250

# print the explanation and preliminary story
def print_the_introduction_story():
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))
    print(s.recv(1500))

# get the g from server
def get_g():
    s.send("g".encode())
    s.settimeout(3.0)
    g = s.recv(50).decode()
    s.settimeout(None)

    s.settimeout(delay_time)
    try:
        junk = s.recv(50).decode()
    except socket.timeout:  # fail after 5 second of no activity
        print("Didn't receive data. Timeout")
    s.settimeout(None)
    return g

# get the current location
def get_location():
    s.send("c".encode())
    s.settimeout(3.5)
    loc = s.recv(50).decode()
    s.settimeout(None)

    s.settimeout(3.3)
    try:
        junk = s.recv(50).decode()
    except socket.timeout:  # fail after 5 second of no activity
        print("Didn't receive data. Timeout")
    s.settimeout(None)

    x = loc.split(',')[0][1:]
    y = loc.split(',')[1][:-2]
    return x, y


# return the possible steps and the walls
def get_possible_steps():
    _, l, r, u, d = get_information()
    ones = []  # possible steps
    zeros = []  # walls
    if l == 1:
        ones.append("l")
    elif l == 0:
        zeros.append("l")
    if r == 1:
        ones.append("r")
    elif r == 0:
        zeros.append("r")
    if u == 1:
        ones.append("u")
    elif u == 0:
        zeros.append("u")
    if d == 1:
        ones.append("d")
    elif d == 0:
        zeros.append("d")
    return ones, zeros


def get_location_after_step(step, x, y):
    if step == 'l':
        x = int(x) - 1
    elif step == 'r':
        x = int(x) + 1
    elif step == 'u':
        y = int(y) + 1
    elif step == 'd':
        y = int(y) - 1
    return x, y


# send a step to go
def do_choice(step):
    s.send(step.encode())
    s.settimeout(delay_time)
    try:
        junk = s.recv(50).decode()
    except socket.timeout:  # fail after 2 second of no activity
        print("Didn't receive data! [Timeout]")
    s.settimeout(None)

    s.settimeout(delay_time)
    try:
        junk = s.recv(50).decode()
    except socket.timeout:  # fail after 5 second of no activity
        print("Didn't receive data! [Timeout]")
    s.settimeout(None)


def take_a_step():
    possible_steps, walls = get_possible_steps()
    # mark the walls in maze
    for step in walls:
        x_new, y_new = [int(ii) for ii in get_location_after_step(step, x, y)]
        if x_new >= 250 or y_new >= 250 or x_new < 0 or y_new < 0:
            continue
        maze[x_new, y_new] = 3
    # mark the steps in maze
    if g.startswith("Your distance"):
        maze[int(x), int(y)] = 2
    else:
        maze[int(x), int(y)] = 1
    options_to_go = []
    for pos_step in possible_steps:
        x_after_step, y_after_step = get_location_after_step(pos_step, x, y)
        if maze[int(x_after_step), int(y_after_step)] == 0:
            options_to_go.append(pos_step)
    if len(options_to_go) > 0:
        do_choice(options_to_go[0])
        print("choice: " + str(options_to_go[0]))
        steps.append(options_to_go[0])
        print("len steps: " + str(len(steps)))
    elif len(options_to_go) == 0:
        do_choice(reverse[steps[-1]])
        print("choice back: " + str(reverse[steps[-1]]))
        del steps[-1]
        print("len steps: " + str(len(steps)))


# get the i from the server
def get_information():
    s.send("i".encode())
    s.settimeout(4.0)
    ans = s.recv(50).decode()
    s.settimeout(None)

    s.settimeout(delay_time)
    try:
        junk = s.recv(50).decode()
    except socket.timeout:  # fail after 5 second of no activity
        print("Didn't receive data! [Timeout]")
    s.settimeout(None)
    l = int(ans[2])
    r = int(ans[7])
    u = int(ans[12])
    d = int(ans[17])
    return ans, l, r, u, d


# find the optional treasure points by one point and the distance
def find_optional_points(known_x, known_y, distance):
    optional_points = []
    for x in range(MAZE_SIZE+1):
        for y in range(MAZE_SIZE+1):
            if math.sqrt((x - known_x) ** 2 + (y - known_y) ** 2) == distance:
                optional_points.append([x, y])
    return optional_points


def find_common_points(options_list):
    common_points = options_list[0]
    for list in options_list:
        for point in common_points:
            if point not in list:
                common_points.remove(point)
    return common_points


# send the solution
def get_s(solution):
    s.send("s".encode())
    s.settimeout(3.0)
    junk = s.recv(50).decode()
    s.settimeout(None)

    s.send(solution.encode())
    s.settimeout(3.0)
    server_ans = s.recv(1000).decode()
    s.settimeout(None)
    print(server_ans)
    s.settimeout(3.0)
    server_ans2 = s.recv(1000).decode()
    s.settimeout(None)
    print(server_ans2)
    server_ans3 = s.recv(1000).decode()
    s.settimeout(None)
    print(server_ans3)

    return server_ans


if __name__ == "__main__":
    s = socket.socket()
    s.connect(('185.229.226.251', 80))
    delay_time = 2.2

    print_the_introduction_story()
    maze = np.zeros((MAZE_SIZE, MAZE_SIZE)) # create the maze matrix

    # define the reverse step of each step
    reverse = {
        "r": "l",
        "l": "r",
        "u": "d",
        "d": "u"}
    steps = []
    options_points = []  # list of lists of optional treasure points for each point and distance

    g = get_g()
    while g.startswith("far") or g.startswith("Your distance") or g.startswith("> What") or g.startswith("("):

        if g.startswith("> What") or g.startswith("("):  # error reading from server
            g = get_g()
            continue

        print("g: " + g)
        x, y = get_location()
        print("location: (" + x + "," + y + ")")

        if g.startswith("Your distance"):  # we are close to the treasure!
            distance = math.sqrt(int(g.rsplit('√ ', 1)[1]))
            options_points.append(find_optional_points(int(x), int(y), distance))

            common_points = find_common_points(options_points)
            if len(common_points) == 1: # the solution
                # find the solution
                get_s(f'{common_points[0][0]},{common_points[0][1]}')
                print('the treasure location:', common_points[0])
                break

        take_a_step()
        g = get_g()












