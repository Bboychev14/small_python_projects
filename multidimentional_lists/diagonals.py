n = int(input())
matrix = []

for _ in range(n):
    numbers = [int(x) for x in input().split(', ')]
    matrix.append(numbers)

main = []
secondary = []

for row in range(n):
    main.append(matrix[row][row])
    secondary.append(matrix[row][n - 1 - row])
print(f"Primary diagonal: {', '.join(str(x) for x in main)}. Sum: {sum(main)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary)}. Sum: {sum(secondary)}")