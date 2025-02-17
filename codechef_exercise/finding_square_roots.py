#the first line of the input contains an integer N, the number of test cases. 
#N lines follow. Each line contains an integer T whose square root needs to be computed.
from cmath import sqrt
import math

n = int(input("Enter number: "))

def square_root(n):
    sqrt = math.sqrt(n)
    print("square root:" , sqrt)


square_root(n)
