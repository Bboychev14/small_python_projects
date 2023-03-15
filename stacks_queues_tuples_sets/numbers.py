first_seq = set([int(x) for x in input().split()])
second_seq = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()
    if command[0] == 'Add' and command[1] == 'First':
        numbers = [int(x) for x in command[2:]]
        for num in numbers:
            first_seq.add(num)
    elif command[0] == 'Add' and command[1] == 'Second':
        numbers = [int(x) for x in command[2:]]
        for num in numbers:
            second_seq.add(num)
    elif command[0] == 'Remove' and command[1] == 'First':
        numbers = [int(x) for x in command[2:]]
        for num in numbers:
            if num in first_seq:
                first_seq.remove(num)
    elif command[0] == 'Remove' and command[1] == 'Second':
        numbers = [int(x) for x in command[2:]]
        for num in numbers:
            if num in second_seq:
                second_seq.remove(num)
    else:
        print(first_seq.issubset(second_seq) or second_seq.issubset(first_seq))
print(*sorted(first_seq), sep=', ')
print(*sorted(second_seq), sep=', ')