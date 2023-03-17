n = int(input())
matrix = []
main = []
secondary = []
for x in range(n):
    numbers = [int(x) for x in input().split()]
    matrix.append(numbers)
    main.append(numbers[x])
    secondary.append(numbers[n - 1 - x])
result = abs(sum(main) - sum(secondary))
print(result)