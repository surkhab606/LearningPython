
operator = input("Please enter +, -, * or /")

if operator == "+":
    add1 = float(input("Please enter the first number you would like to add: "))
    add2 = float(input("Please enter the second number you would like to add: "))
    addresult = add1 + add2
    print(f"The result is: {addresult}")

elif operator == "-":
    sub1 = float(input("Please enter the first number you would like to subtract: "))
    sub2 = float(input("Please enter the second number you would like to subtract: "))
    subresult = sub1 - sub2
    print(f"The result is: {subresult}")

elif operator == "*":
    multi1 = float(input("Please enter the first number you would like to multiply: "))
    multi2 = float(input("Please enter the second number you would like to multiply: "))
    multiresult = multi1 * multi2
    print(f"The result is: {multiresult}")

else:
    div1 = float(input("Please enter the first number you would like to divide: "))
    div2 = float(input("Please enter the second number you would like to divide: "))
    divresult = div1 / div2
    print(f"The result is: {divresult}")
