rows, cols = [int(x) for x in input().split()]
word = input()
matrix = []
ind = 0

for row in range(rows):
    row_elements = []
    for col in range(cols):
        row_elements.append(word[ind % len(word)])
        ind += 1
    if row % 2 != 0:
        print(''.join(reversed(row_elements)))
    else:
        print(''.join(row_elements))