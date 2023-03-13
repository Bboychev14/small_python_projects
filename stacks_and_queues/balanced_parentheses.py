text = input()
opening = []
closing = []
result = 'YES'

for letter in text:
    if letter in '([{':
        opening.append(letter)
    else:
        closing.append(letter)
closing.reverse()
if len(opening) == 0:
    result = 'No'
for _ in range(len(opening)):
    if len(opening) != len(closing) or len(opening) == 0:
        result = 'NO'
        break
    if opening[-1] == '(' and closing[-1] != ')':
        result = 'NO'
        break
    elif opening[-1] == '[' and closing[-1] != ']':
        result = 'NO'
        break
    elif opening[-1] == '{' and closing[-1] != '}':
        result = 'NO'
        break
    closing.pop()
    opening.pop()
print(result)