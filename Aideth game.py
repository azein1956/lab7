#The structure of Try 1 loop needs to be edited by developer. It should not exit the else while loop
#when number is less than 500, it should loop back from the starting while loop and exit until it is true.
#Because Try 1 is using OR logic by nesting the false value (similar to nesting control statement) and
# should get the same results in looping as in Try 2 while loop below using traditional OR logic.
#Try 1:
number = int(input("Enter a number between 100 and 500: "))
while number < 100:
    print("Number entred is less than 100.")
    number = int(input("Enter a number between 100 and 500: "))
else:
    while number > 500:
        print("Number entred is greater than 500.")
        number = int(input("Enter a number between 100 and 500: "))

    else:
        print("Number is between 100 and 500")
"""        
#Try 2:
number = int(input("Enter a number between 100 and 500: "))
while number < 100 or number > 500:
    number = int(input("Enter a number between 100 and 500 to exit the loop: "))
else:
    print("Number is between 100 and 500")
"""





