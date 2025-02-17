
q = int(input("Enter number: "))


def is_palindrom(q):

    temp = q
    reverse = 0

    while n > 0:
        dig = n % 10
        reverse = reverse * 10 + dig
        n = n // 10

    if temp == reverse:
        print("WIN!")
    else:
        print("LOSE...")


is_palindrom(q)
