#Guess the admission to Med school, Grades should be greater than 98 AND MCAT score is greater than 95.
grades = int(input('Enter total grades: '))
mcat_score = int(input('Enter MCAT score: '))
while grades < 98:
        print('\n Did not guess the grades ')
        grades = int(input('Please guess total grades: '))
while mcat_score < 95: #AND MCAT should not be be less than 95
    print("\n Did not guess the MCAT scores")
    mcat_score = int(input('Please guess MCAT score:  '))
else:
        print("\n Your guess is correct.")
print("Good Bye")