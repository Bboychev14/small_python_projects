n = int(input())
matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    damage = matrix[row][col]
    for x in range(row -1, row + 2):
        for y in range(col - 1, col + 2):
            if 0 <= x < n and 0 <= y < n and matrix[x][y] > 0:
                matrix[x][y] -= damage

alive_cells = 0
cells_sum = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells += 1
            cells_sum += matrix[row][col]
print(f"Alive cells: {alive_cells}")
print(f"Sum: {cells_sum}")
for row in matrix:
    print(*row)