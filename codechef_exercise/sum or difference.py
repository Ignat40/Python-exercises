# write a progmram to take two numbers as an input and print their difference 
# if the first number is greater than the second number otherwise print their sum


a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))

def checker(a, b):
    if a > b:
        print(a - b)
    else:
        print(a + b)


checker(a, b)