yearOfBirth = {'Alicia': 1997, 'Marie': 1953, 'Samuel': 2010}
ages = dict()
print("Marie was born in", yearOfBirth['Marie'])
# Adding new entries to a dictionary:
ages['Marek'] = 37
ages['Michaela'] = 23
ages['Imani'] = 12
print(ages)
# Updating an entry:
print("Imani has a birthday!")
ages['Imani'] = ages['Imani'] + 1
print("She is now", ages['Imani'], 'years old')