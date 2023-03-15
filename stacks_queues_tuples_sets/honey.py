from collections import deque
bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
symbols = deque([x for x in input().split()])
total_honey = 0
while bees and nectars:
    temp_honey = 0
    bee = bees[0]
    nectar = nectars.pop()
    if nectar >= bee:
        bees.popleft()
        symbol = symbols.popleft()
        if symbol == '+':
            temp_honey = bee + nectar
        elif symbol == '-':
            temp_honey = bee - nectar
        elif symbol == '*':
            temp_honey = bee * nectar
        else: # symbol = /
            if bee == 0 or nectar == 0:
                continue
            temp_honey = bee / nectar
        if temp_honey == 0:
            continue
        total_honey += abs(temp_honey)
print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectars:
    print(f"Nectar left: {', '.join(str(x) for x in nectars)}")