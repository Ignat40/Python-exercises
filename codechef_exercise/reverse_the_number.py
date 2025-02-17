#Given an Integer N, write a program to reverse it.

num = int(input("Enter the number you want to reverse: "))



def reverse_number(num):

    rev_num = 0

    while num > 0:
        remainder = num % 10
        rev_num = rev_num * 10 + remainder
        num = num // 10

    print("REVERSED: ", rev_num)


reverse_number(num)


  
