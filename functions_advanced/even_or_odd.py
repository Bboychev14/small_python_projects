def even_odd(*args):
    list = []
    for x in args:
        list.append(x)
    command = list.pop()
    parity = 0 if command == 'even' else 1
    return [x for x in list if x % 2 == parity]
