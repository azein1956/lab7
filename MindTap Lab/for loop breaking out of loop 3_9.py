for num in range(10, 100):
    if num == 0:
        continue
    elif num % 5 != 0:
        continue
    elif type(num) != int:
        continue
    elif num == 95:
        break
    else:
        pass
        print("num = ", num)