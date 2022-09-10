# Write your code here
def skip_integers(*number):
    for i in number:
        if type(i) == int:
            continue
        else:
            print(i)
# Test you code here
skip_integers(3, 5.2, "value", 6.0)