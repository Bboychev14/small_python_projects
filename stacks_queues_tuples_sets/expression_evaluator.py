from collections import deque
text = input().split()
numbers = deque()

for symbol in text:
    if symbol in '+-*/':
        while len(numbers) > 1:
            result = 0
            num_1 = numbers.popleft()
            num_2 = numbers.popleft()
            if symbol == '+':
                result = num_2 + num_1
            elif symbol == '-':
                result = num_1 - num_2
            elif symbol == '*':
                result = num_1 * num_2
            elif symbol == '/':
                result = num_1 // num_2
            numbers.appendleft(result)

    else:
        numbers.append(int(symbol))
print(numbers[0])