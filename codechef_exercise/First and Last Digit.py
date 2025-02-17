# If Give an integer N . 
# Write a program to obtain the sum of 
# the first and last digits of this number.


n = int(input("Enter value for N: "))

def first_digit(n) :

    while n >= 10:
        n = n//10
    return n
    
def last_digit(n):

    n = n % 10
    return n


   
if __name__ == '__main__':

    
    print("The sum of the f and l digits is:", first_digit(n), "+" , last_digit(n), "=" ,first_digit(n)+last_digit(n))
