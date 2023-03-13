from collections import deque
cups_capacity = deque(int(x) for x in input().split())
bottles_capacity = [int(x) for x in input().split()]
wasted_litters = 0

while cups_capacity and bottles_capacity:
    cup = cups_capacity[0]
    bottle = bottles_capacity[-1]
    if cup > bottle:
        cups_capacity[0] -= bottles_capacity.pop()
    elif cup == bottle:
        cups_capacity.popleft()
        bottles_capacity.pop()
    else: #cup < bottle
        wasted_litters += bottle - cup
        cups_capacity.popleft()
        bottles_capacity.pop()

if len(cups_capacity) == 0:
    print("Bottles:", end=' ')
    for bottle in bottles_capacity:
        print(bottle, end=' ')
else: #bottles = 0
    print('Cups:', end=' ')
    for cup in cups_capacity:
        print(cup, end=' ')
print(f"\nWasted litters of water: {wasted_litters}")