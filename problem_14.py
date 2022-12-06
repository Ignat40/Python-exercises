# In this kata you will create a function 
# that takes a list of non-negative integers
#  and strings and returns a new list 
#  with the strings filtered out.



l = [1,2,'aasf','1','123',123]
new_list = []

def filter_list(l):

    new_list = [x for x in l if isinstance(x, (int, float))]
    print(new_list)


    # for x in l:
    #     if type(x) != str:
    #         new_list.append(x)
    # return new_list
  
   

filter_list(l)

