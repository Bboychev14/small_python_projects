from collections import deque
green = int(input())
yellow = int(input())
command = input()
cars = deque()
passed_cars = 0
crash = False

while command != 'END':
    if command != 'green':
        cars.append(command)
    else:
        temp_green = green
        while cars and temp_green > 0:
            car = cars.popleft()
            if len(car) > temp_green + yellow:
                index = temp_green + yellow
                print("A crash happened!")
                print(f"{car} was hit at {car[index]}.")
                crash = True
                break
            else: # len(car) <= temp_green + yellow:
                passed_cars += 1
                temp_green -= len(car)
    if crash:
        break

    command = input()
if not crash:
    print(f"""Everyone is safe.
{passed_cars} total cars passed the crossroads.""")