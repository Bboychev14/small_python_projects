from collections import deque


def time_converter(time):
    hours, minutes, seconds = starting_time
    return seconds + minutes * 60 + hours * 3600


def final_time(seconds):
    seconds %= 24 * 60 * 60
    h = seconds // 3600
    m = seconds % 3600 // 60
    s = seconds % 3600 % 60
    return '{:02d}:{:02d}:{:02d}'.format(h, m, s)


robot_name_time = input().split(';')
starting_time = [int(x) for x in input().split(':')]
time_in_seconds = time_converter(starting_time)
command = input()
products = deque()

while command != 'End':
    products.append(command)
    command = input()
robots_times_to_proceed = {}
busy_until = {}

for robot in robot_name_time:
    name, time = robot.split('-')
    robots_times_to_proceed[name] = int(time)
    busy_until[name] = 0

while products:
    product = products.popleft()
    time_in_seconds += 1
    for robot in busy_until:
        if busy_until[robot] <= time_in_seconds:
            busy_until[robot] = 0
            busy_until[robot] += robots_times_to_proceed[robot] + time_in_seconds
            print(f"{robot} - {product} [{final_time(time_in_seconds)}]")
            break
    else:
        products.append(product)
