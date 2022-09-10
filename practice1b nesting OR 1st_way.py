user_name = input("Enter your name: ")
quantity_purchased = int(input("Enter number of packages purchased: "))
package_retail = 95
if quantity_purchased <= 10:
    discount = 0
else:
    if quantity_purchased <= 19:
        discount = 20
    else:
        if quantity_purchased <= 49:
            discount = 30
        else:
            if quantity_purchased <= 99:
                discount = 40
            else:
                if quantity_purchased >= 100:
                    discount = 50
amount_of_discount = (package_retail*quantity_purchased * discount)/ 100
print("Welcome back ", user_name)
print("Number of packages purchased by the user: ", quantity_purchased)
print("Quatity percent discount: ", discount, "%")
print("Amount of discount is: ", amount_of_discount)
print("Amount after discount: ", (package_retail * quantity_purchased) - amount_of_discount)

