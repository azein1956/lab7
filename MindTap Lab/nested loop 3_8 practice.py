numList = [55, 23, 71, 2, 15]
i = 0
sum = 0
while i < len(numList):
    sum += numList[i]
    if sum > 100:
        break
print("Final value of sum and i:", sum, i)
