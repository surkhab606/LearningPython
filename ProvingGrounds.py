
age = int(input("Enter a number between 1 and 10: "))

while age < 1 or age > 10:
   age = int(input("Please do not enter an invalid number. Try again: "))

print(f"Thank you. Your age is now {age} years old.")