fruits = ["apple", "orange", "pomegranate"]
vegetables = ["carrot", "broccoli", "celery"]
meats = ["pepperoni", "beef", "chicken"]

groceries = [fruits, vegetables, meats]

for foodType in groceries:
    for food in foodType:
        print(food, end=" ")
    print()
