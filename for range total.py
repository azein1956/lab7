total_sum = 0
r1 = range(5,55)
for x in range(5, 55, 2):
    total_sum = total_sum + (x + 1)
    print(x+1, "+", total_sum - (x + 1), "=", total_sum)