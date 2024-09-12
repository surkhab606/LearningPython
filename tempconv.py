userInput = int(input("Press 1 to convert C to F. Press 2 to convert F to C. "))

if userInput == 1:
    prompt1 = (float(input("What is the temperature you would like to convert? ")))
    result1 = round(prompt1 * 1.8 + 32, 1)
    print(f"The temperature you inputted in Fahrenheit is: {result1} Fahrenheit")

elif userInput == 2:
    prompt2 = (float(input("What is the temperature you would like to convert? ")))
    result2 = round((prompt2 - 32) / 1.8, 1)
    print(f"The temperature you inputted in Celsius is: {result2} Celsius")

else:
    print("Invalid input.")

