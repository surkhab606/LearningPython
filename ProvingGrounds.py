
rows = int(input("Please enter the number of rows: "))
columns = int(input("Please enter the number of columns: "))
symbol = input("Please enter a symbol: ")


for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()

