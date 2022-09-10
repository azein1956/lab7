"""
Write a script that takes a whole number
from a user’s input and prints out its
2's multiplication table till 10.
"""
whole_num = int(input("Generate a Multiplication table for: "))
print("_" * 10)
print("Number: ", whole_num)
for i in range(1,6):
    print(i * 2, ": ", (i * 2) * whole_num)
print("_" * 10)