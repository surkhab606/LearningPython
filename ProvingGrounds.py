fruit = ["pineapple"]
johnson = ["johnson"]
car = ["camaro"]
total = [fruit, johnson, car]

for element in total:
    for sub_element in element:
        print(sub_element, end="")
    print()