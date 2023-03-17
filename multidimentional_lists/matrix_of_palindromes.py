rows, cols = [int(x) for x in input().split()]
for row in range(rows):
    temp_list = []
    for col in range(cols):
        temp_symbol = chr(97 + row) + chr(97 + col + row) + chr(97 + row)
        temp_list.append(temp_symbol)
    print(' '.join(temp_list))
    temp_list.clear()