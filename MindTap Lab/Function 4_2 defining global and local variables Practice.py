#Function 4.2 defining global and local variables
number = 5
def summation(first, second):
    total = 9 + 5 #+ second #+ number
    totalx = 17
    return totalx
outer_total = summation(10, 20)
print("The first number we initialized was " + str(number))
print("The total after summation is " + str(outer_total))