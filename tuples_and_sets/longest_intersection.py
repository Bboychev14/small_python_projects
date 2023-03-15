def gen_numbers(x):
    start, end = [int(x) for x in x.split(',')]
    return set(range(start, end + 1))


n = int(input())
longest = []
for _ in range(n):
    numbers = input().split('-')
    first_set = gen_numbers(numbers[0])
    second_set = gen_numbers(numbers[1])
    temp = first_set.intersection(second_set)
    if len(temp) > len(longest):
        longest = temp
result = [x for x in longest]
print(f"Longest intersection is {result} with length {len(longest)}")