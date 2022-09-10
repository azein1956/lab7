string = input("Enter a string: ")
size = len(string)
i = 0
# iterate loop till the last character
while i < size:
    # break loop if current character is number
    if string[i].isdecimal():
        break;
    # print current character
    print(string[i], end=" ") #use end=" " tp print string horizontaly
    i = i + 1

