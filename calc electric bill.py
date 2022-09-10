amount = 0
num_of_units = int(input("Enter number of electric unit: "))
if num_of_units <= 100:
    print("You pay: ", float(amount))
else:
    if num_of_units <= 200:
        amount = (num_of_units-100) * 5
        print("You pay: ", float(amount))
    else:
        if num_of_units > 200:
            amount = 500 + (num_of_units - 200) * 10
            print("You pay: ", float(amount))