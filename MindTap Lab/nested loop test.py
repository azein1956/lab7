# Write your code here
for i in range(10, 100):
    if i == 95:
        break
    else:
        if i % 5 == 0:
            print(i)
        else:
            if type(i) != int:
                continue
            else:
                pass