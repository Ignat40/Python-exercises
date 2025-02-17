""" Pooja would like to withdraw X $US from an ATM. 
The cash machine will only accept the transaction 
if X is a multiple of 5, and Pooja's 
account balance has enough cash to perform 
the withdrawal transaction (including bank charges). 
For each successful withdrawal the bank charges 0.50 $US.
 Calculate Pooja's account balance after an attempted transaction. """

available_cash = 120
x = float(input("Enter the amount you want to withdraw:"))
bank_charges = 0.50


if x % 5 == 0:
    available_cash = available_cash - (x + bank_charges)
    print(available_cash)
elif x > available_cash:
    print("Not enough money on this account. Please enter another amount...")
else:
    print("Invalid ammount...")

