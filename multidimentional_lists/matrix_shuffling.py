def is_inside(row, col, rows, cols):
    return 0 <= row < rows and col >= 0 and col < cols


rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append(input().split())

command = input()
while command != 'END':
    command = command.split()
    if command[0] != 'swap' or len(command) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in command[1:]]
    if is_inside(row1, col1, rows, cols) and is_inside(row2, col2, rows, cols):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in matrix:
            print(' '.join(row))
    else:
        print(f"Invalid input!")
    command = input()