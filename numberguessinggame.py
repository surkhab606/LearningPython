import random

user_range = int(input("Please enter the first number in the range of numbers you would like: "))
user_range2 = int(input("Please enter the second number in the range of numbers you would like: "))

comp_number = random.randint(user_range, user_range2)

print(f"The Computer has selected a random number within your range of {user_range} to {user_range2}.")
user_guess = int(input("Please guess the number: "))

while user_guess != comp_number:

    while user_guess < user_range or user_guess > user_range2:
        print("Out of bounds. Try again!")
        user_guess = int(input("Please guess the number: "))

    if user_guess > comp_number:
        print("Too high! Try again!")
        user_guess = int(input("Please guess the number: "))

    if user_guess < comp_number:
        print("Too low! Try again!")
        user_guess = int(input("Please guess the number: "))

print(f"You got it! The number was {comp_number}")
