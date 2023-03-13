clothes = [int(x) for x in input().split()]
capacity = int(input())
racks_needed = 0
temp_num = 0
while clothes:
    if temp_num + clothes[-1] > capacity:
        racks_needed += 1
        temp_num = 0
        continue
    elif temp_num + clothes[-1] == capacity:
        racks_needed += 1
        temp_num = 0
        clothes.pop()
    else:
        temp_num += clothes.pop()
if temp_num > 0:
    racks_needed += 1
print(racks_needed)