import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 100)


def get_attempts(diff_str):
    if diff_str == 'easy':
        return 10
    elif diff_str == 'hard':
        return 5
    return get_attempts(input("Wrong input. Choose 'easy' or 'hard': "))


attempts = get_attempts(difficulty)

you_lose = True
for _ in range(attempts):
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts -= 1
    guess = int(input("Make a guess: "))
    if guess > number:
        print("Too high.\nGuess again.")

    elif guess < number:
        print("Too low.\nGuess again.")

    else:
        you_lose = False
        print("You win!")
        break

if you_lose:
    print("You lose!")
