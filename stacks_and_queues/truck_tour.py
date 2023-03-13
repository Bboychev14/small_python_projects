from collections import deque
petrol_pumps = int(input())
information = deque()

for _ in range(petrol_pumps):
    petrol_distance = [int(x) for x in input().split()]
    information.append(petrol_distance)
for tries in range(petrol_pumps):
    tank = 0
    fail = False
    for petrol, distance in information:
        tank += petrol
        if tank < distance:
            information.append(information.popleft())
            fail = True
            break
        else:
            tank -= distance
    if not fail:
        print(tries)
        break