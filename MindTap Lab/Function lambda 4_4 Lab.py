num = [44, 5, 8, 2, 11, 2, 5, 7, 16]
for x in num:
    if num.count(x) > 1:
        pos = num.index(x)
        num.pop(pos)
    else:
        pass
print(num)