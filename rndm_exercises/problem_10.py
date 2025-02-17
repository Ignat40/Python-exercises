#A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000.
#Ask the user for quantity
#Suppose, one unit wil lcost 100.
#Judge and print the total cost for user

quantity = float(input("Enter quantitiy: "))

def discount(quantity):
    if quantity < 1000:
        print("Final sum: ", quantity)
    else:
        print("Final sum: ", quantity - 1000 / 10)

discount(quantity)


