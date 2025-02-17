#Given the list of numbers, you are to sort them in non decreasing order.

list = [13, 17, 85, 49, 66, 25, 46, 65, 4, 100, 1, 71, 44, 12, 50, 62, 33, 82, 47, 36]


for i in range(len(list)):
    for j in range(len(list)):
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]

print(list) 















# of course we can always use the sort method

# list.sort()
# print (list)
