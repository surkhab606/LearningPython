import random

result = int(input("Press 1 to pick a number between two intervals, and Press 2 to generate a random number. "))

if result == 1:

    point1 = int(input("Please enter first interval end point: "))
    point2 = int(input("Please enter second interval end point: "))

    print(random.randint(point1, point2))

elif result == 2:

    print("Your random number is: ")
    print(random.random())

else:
    print("Invalid input.")





