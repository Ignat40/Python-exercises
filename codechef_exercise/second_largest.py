# Three numbers A, B and C are the inputs. 
# Write a program to find second largest among them

a = int(input("Enter value for A: "))
b = int(input("Enter value for B: "))
c = int(input("Enter value for C: "))

def second_biggest(a, b, c):

    if a > b and a > c:
        
        if b > c:
            print (b)
        else:
            print (c)
    
    elif b > a and b > c:
        
        if c > a:
            print (c)
        else:
            print (a)

    elif a > b:
        print(a)
    else:
         print(b) 
    
        


second_biggest(a, b, c)

    