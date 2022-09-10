def max(x, y, z):
    if x > y:
        if x > z:
            print("Max is: ", x)
        else:
            if z > x:
                if z > y:
                    print("Max is: ", z)
    else:
        if y > x:
            if y > z:
                print("Max is: ", y)
        
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
max(num1, num2, num3)