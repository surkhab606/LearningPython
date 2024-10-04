import random

low = 1
high = 100
guess_count = 0
number = random.randint(low, high)

user_guess = int(input("Please guess a number between 1 and 100: "))

while user_guess != number:

    if number < user_guess <= 100:
        print("Too high! Try again!")
        user_guess = int(input("Please guess a number between 1 and 100: "))
        guess_count += 1

    elif number > user_guess >= 1:
        print("Too low! Try again!")
        user_guess = int(input("Please guess a number between 1 and 100: "))
        guess_count += 1

    else:
        print("Invalid input. Try again.")
        user_guess = int(input("Please guess a number between 1 and 100: "))
        guess_count += 1

print(f"You got it! It took you {guess_count} guesses!")
