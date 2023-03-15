n, m = [int(x) for x in input().split()]
set_n = set()
set_m = set()
for i in range(n + m):
    number = int(input())
    if i < n:
        set_n.add(number)
    else:
        set_m.add(number)
result = set_n.intersection(set_m)
for x in result:
    print(x)