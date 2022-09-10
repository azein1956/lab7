cars = ("coupe", "coupe", "coupe", "carbiolet", "sedan")
fav = cars.count("coupe")
print(fav)
amt = len(cars)
print(amt)
if ((fav * 100) / amt) > 45:
    print("Too many coupes in the garage.")
else:
    print("You are all set with cars.")
    
