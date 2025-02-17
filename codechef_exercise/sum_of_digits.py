# You're given an integer N. 
# Write a program to calculate the sum of all the digits of N.

N = input("Enter value for N: ")

def sum_digits(N):

    sum = 0
    for digits in str(N):
        sum += int(digits)
    print("The sum is: ", sum)

sum_digits(N)

