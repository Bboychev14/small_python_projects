def cheking(row, col):
    if matrix[row][col] == 'e':
        print(f"Game over! ({row}, {col})")
        return True


def found_coal(row, col):
    if matrix[row][col] == 'c':
        matrix[temp_row][temp_col] = '*'
        return True


n = int(input())
directions = input().split()
matrix = []

temp_row = 0
temp_col = 0
total_coal = 0
temp_coal = 0
success = False
end = False
for row in range(n):
    line = input().split()
    for element in line:
        if element == 'c':
            total_coal += 1
        elif element == 's':
            temp_row = row
            temp_col = line.index(element)
    matrix.append(line)

for direction in directions:
    if direction == 'left' and temp_col - 1 >= 0:
        temp_col -= 1
        if cheking(temp_row, temp_col):
            end = True
            break
        elif found_coal(temp_row, temp_col):
            temp_coal += 1
    elif direction == 'right' and temp_col + 1 < n:
        temp_col += 1
        if cheking(temp_row, temp_col):
            end = True
            break
        elif found_coal(temp_row, temp_col):
            temp_coal += 1
    elif direction == 'up' and temp_row - 1 >= 0:
        temp_row -= 1
        if cheking(temp_row, temp_col):
            end = True
            break
        elif found_coal(temp_row, temp_col):
            temp_coal += 1

    elif direction == 'down' and temp_row + 1 < n:
        temp_row += 1
        if cheking(temp_row, temp_col):
            end = True
            break
        elif found_coal(temp_row, temp_col):
            temp_coal += 1
    if temp_coal == total_coal:
        success = True
        print(f"You collected all coal! ({temp_row}, {temp_col})")
        break

if not success and not end:
    print(f"{total_coal - temp_coal} pieces of coal left. ({temp_row}, {temp_col})")