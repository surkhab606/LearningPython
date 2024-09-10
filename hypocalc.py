import math

a = float(input("Please enter the first side of the triangle: "))
b = float(input("Please enter the second side of the triangle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"The hypotenuse given your dimensions is equal to: {c}")
