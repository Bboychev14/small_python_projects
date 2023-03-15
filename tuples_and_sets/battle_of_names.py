n = int(input())
odd = set()
even = set()
result = []
for row in range(1, n + 1):
    name = [ord(x) for x in input()]
    temp = sum(name)
    odd_even = temp // row
    if odd_even % 2 == 0:
        even.add(odd_even)
    else:
        odd.add(odd_even)
if sum(odd) == sum(even):
    result = odd.union(even)
    print(', '.join(str(x) for x in result))
elif sum(odd) > sum(even):
    result = odd.difference(even)
    print(', '.join(str(x) for x in result))
else:
    result = even.symmetric_difference(odd)
    print(', '.join(str(x) for x in result))