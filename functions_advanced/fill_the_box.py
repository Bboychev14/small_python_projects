def fill_the_box(*args):
    volume = args[0] * args[1] * args[2]
    cubes = 0
    for index in range(3, len(args) - 1):
        if args[index] == 'Finish':
            break
        cubes += args[index]

    if volume > cubes:
        return f"There is free space in the box. You could put {volume - cubes} more cubes."

    else:
        return f"No more free space! You have {cubes - volume} more cubes."


print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
