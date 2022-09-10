def max(a, b, c):
    if a > b:
        if a > c:
            print("Max is: ", a)
            
    if b > a:
            if b > c:
                print("Max is: ", b)
            
    if c > a:
        if c > b:
            print("Max is: ", c)
      

a, b, c = input("Enter num1 values: ").split()
max(int(a), int(b), int(c))
#n1, n2, n3 = [int(n1) for n1 in input("Enter three values: ").split()]
#max(n1, n2, n3)