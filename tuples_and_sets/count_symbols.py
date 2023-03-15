text = input()
occ = {}
for letter in text:
    if letter not in occ:
        occ[letter] = 0
    occ[letter] += 1
for k, v in sorted(occ.items()):
    print(f"{k}: {v} time/s")