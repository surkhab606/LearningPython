decision = int(input("Please type 1 if you would like to convert pounds to kilograms or type 2 if you would like to "
                     "convert kilograms to pounds: "))

if decision == 1:
    userPounds = float(input("Please enter the weight you would like to convert: "))
    resultKilograms = round(userPounds * 0.45359237)
    print(f"{userPounds} is equal to: {resultKilograms} kilograms.")

elif decision == 2:
    userKilograms = float(input("Please enter the weight you would like to convert: "))
    resultPounds = round(userKilograms * 2.2)
    print(f"{userKilograms} is equal to: {resultPounds} pounds.")


else:
    print("What.")