from collections import deque
materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
presents = []

while materials and magic:
    temp_material = materials.pop()
    temp_magic = magic.popleft()
    product = temp_magic * temp_material
    if product == 150:
        presents.append("Doll")
    elif product == 250:
        presents.append("Wooden train")
    elif product == 300:
        presents.append("Teddy bear")
    elif product == 400:
        presents.append("Bicycle")
    else:
        if product < 0:
            materials.append(temp_material + temp_magic)
        elif product > 0:
            materials.append(temp_material + 15)
        else: # product = 0
            if temp_material != 0:
                materials.append(temp_material)
            if temp_magic != 0:
                magic.appendleft(temp_magic)

if "Doll" and "Train" in presents or "Teddy bear" and "Bicycle" in presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
presents = sorted(presents)
present_count = {}
for present in presents:
    if present not in present_count:
        present_count[present] = 0
    present_count[present] += 1
for kv in present_count:
    print(f"{kv}: {present_count[kv]}")