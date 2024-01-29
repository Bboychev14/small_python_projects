from math import ceil


def leftToRight(matrix, counter):
    size = len(matrix)
    changed = False
    for row in range(size // 2 + 1):
        for col in range(row, size - 1 - row):
            if matrix[row][col] != 0:
                break
            matrix[row][col] = counter
            counter += 1
            changed = True
            if counter >= 10:
                counter = 1
        if changed:
            return counter
    return counter


def rightToLeft(matrix, counter):
    size = len(matrix)
    changed = False
    for row in range(size - 1, size // 2 - 1, -1):
        for col in range(row, size - 1 - row, -1):
            if matrix[row][col] != 0:
                break
            matrix[row][col] = counter
            counter += 1
            changed = True
            if counter >= 10:
                counter = 1
        if changed:
            return counter
    return counter


def upToDown(matrix, counter):
    size = len(matrix)
    changed = False
    for col in range(size - 1, size // 2 - 1, -1):
        for row in range(size - 1 - col, col):
            if matrix[row][col] != 0:
                break
            matrix[row][col] = counter
            counter += 1
            changed = True
            if counter >= 10:
                counter = 1
        if changed:
            return counter
    return counter


def downToUp(matrix, counter):
    size = len(matrix)
    changed = False
    for col in range(size // 2):
        for row in range(size - 1 - col, col, - 1):
            if matrix[row][col] != 0:
                break
            matrix[row][col] = counter
            counter += 1
            changed = True
            if counter >= 10:
                counter = 1
        if changed:
            return counter
    return counter


n = 6
matrix = [[0] * n for x in range(n)]

reps = ceil(n / 2)
counter = 1
for i in range(reps):
    counter = leftToRight(matrix, counter)
    counter = upToDown(matrix, counter)
    counter = rightToLeft(matrix, counter)
    counter = downToUp(matrix, counter)
if n % 2 != 0:
    center = int(n / 2)
    matrix[center][center] = counter

for l in matrix:
    print(l)