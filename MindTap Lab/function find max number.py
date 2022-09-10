def max(a, b, c):
    if a > b:
        if a > c:
            print("Max is: ", a)
            
    
    if c > a:
        if c > b:
            print("Max is: ", c)
            
    if b > a:
        if b > c:
            print("Max is: ", b)



n1, n2, n3 = input("Enter num1 values: ").split()
max(int(n1), int(n2), int(n3))

