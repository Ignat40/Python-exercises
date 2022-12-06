# Task 1. - print the length of a string

def string_length():

    string = str("The quick brown fox jumped over the lazy dog")    
    length = len(string)
    print(length)


# Task 2. - print the character at a specific index

def character_index():

    string = str("The lazy dog jumped over the quick brown fox")
    print(string[1], string[2], string[4], string[4], string[10])

# Task 3. - reverse a string
    
def reverse_string():

    #Faster way ->  print(string[::-1])

    string = str("xof nworb eht revo depmuj god yzal ehT")
    rev_str = ""

    for i in string:
        rev_str = i + rev_str
    print(rev_str)


# Task 4. - print the first and last three characters from a string

def first_and_last_3():

    string = str("The world will eventually come to its end")
    length = len(string)
    first_3 = string[0 : 3]
    last_3 = string[length -3:]
    print(first_3, last_3)




if __name__ == "__main__":
    string_length()
    character_index()
    reverse_string()
    first_and_last_3()