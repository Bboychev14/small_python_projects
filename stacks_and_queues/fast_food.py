from collections import deque
quantity_of_food = int(input())
orders = deque([int(x) for x in input().split()])
biggest_order = max(orders)
flag = False
while orders:
    current_order = orders[0]
    if current_order > quantity_of_food:
        flag = True
        break
    quantity_of_food -= current_order
    orders.popleft()
print(biggest_order)
if flag:
    print('Orders left:', end=' ')
    for x in orders:
        print(x, end=' ')
else:
    print("Orders complete")