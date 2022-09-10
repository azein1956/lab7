#The reason for nesting is when we have to evaluate for logics AND, OR
husband_age = int(input("Enter your age: "))
wife_age = int(input("Enter spouse age: "))
if husband_age > 66:
    if wife_age >65:
        print("Eligible for Tax break")
    else:
        print("Not eligible. Wife's age is less than 66")
else:
    print("Not eligible. Husband's age is less than 66")