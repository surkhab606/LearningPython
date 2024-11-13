
new_list = ["Johnson", "Canyon", "Mountain", "Leaf-Springs"]


age = int(input("Please enter their age: "))


while age < 0:
    print("Invalid input. Please try again.")
    age = int(input("Please enter their age: "))

if 0 <= age <= 5:
    print("Baby!")

elif 6 <= age <= 10:
    print("Kid!")

elif 11 <= age <= 13:
    print("Tween!")

elif 14 <= age <= 17:
    print("Teen!")

elif 18 <= age <= 25:
    print("Young Adult!")

elif 26 <= age <= 40:
    print("Adult!")