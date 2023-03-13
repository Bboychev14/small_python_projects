stack = []
n = int(input())
result = []
for x in range(n):
    command = input()
    if '1 ' in command:
        number = int(command.replace('1 ', ''))
        stack.append(number)
    elif command == '2':
        if stack:
            stack.pop()
    elif command == '3':
        if stack:
            print(max(stack))
    else:
        if stack:
            print(min(stack))
for x in range(len(stack)):
    result.append(stack.pop())
result = [str(x) for x in result]
result = ', '.join(result)
print(result)