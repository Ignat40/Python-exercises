#You are asked to calculate factorials of some small positive integers.

f = int(input("Enter the number you want to factoriel: "))


def find_factorial(f):
    
    factoriel = 1

    for i in range(1, f + 1):
        factoriel *= i
    print(factoriel)

find_factorial(f)