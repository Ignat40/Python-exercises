#reverse a number

# WAY NUMBER ONE:

def python_reverse():
    number = 12345
    number_string = str(number)
    print(str(number_string[::-1]))

# WAY NUMBER TWO:

def while_reverse():
    number = 54321
    reversed_number = 0

    while number != 0:

        current_digit = number % 10
        reversed_number = 10 * reversed_number
        reversed_number += current_digit
        number = number // 10

    print(str(reversed_number))


# WAY NUMBER THREE

def for_reverse():
    number = 28008
    str_number = str(number)
    reversed_number = ''

    for i in range(len(str_number), 0, -1):
        reversed_number += str_number[i - 1]
    print(reversed_number)    

if __name__ == '__main__':

    python_reverse()
    while_reverse()
    for_reverse()