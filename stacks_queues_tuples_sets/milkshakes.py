from collections import deque
chocolate = [int(x) for x in input().split(', ')]
milk = deque([int(x) for x in input().split(', ')])
milkshakes = 0
while chocolate and milk and milkshakes < 5:
    if milk[0] < 1:
        milk.popleft()
    if chocolate[-1] < 1:
        chocolate.pop()
    if chocolate and milk:
        cup_of_milk = milk.popleft()
        if cup_of_milk == chocolate[-1]:
            milkshakes += 1
            chocolate.pop()
        else:
            milk.append(cup_of_milk)
            chocolate[-1] -= 5
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print("Milk: empty")
