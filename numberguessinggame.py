import random

low = 1
high = 100
guess = random.randint(low, high)

userGuess = int(input("Please guess a number between 1 and 100: "))

while userGuess != guess:
    if userGuess > guess:
        print("Too high! Guess again!")
        userGuess = int(input("Please guess a number between 1 and 100"))

    elif userGuess < guess:
        print("Too low! Guess again!")
        userGuess = int(input("Please guess a number between 1 and 100"))

    else:
        print("Invalid input. Guess again")
        userGuess = int(input("Please guess a number between 1 and 100"))

print("You got it!")