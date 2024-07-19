# def multiply(*args):

#     total = 1 

#     for arg in args: 
#         total = total * arg

#     return total



# def apply(*args, operator):

#     if operator == "+":
#         return sum(args)
    
#     elif operator == "*":
#         return multiply(*args)  #mandatory to use * here, as it unpacks the tuple and passes it on to the multiply function 
    
#     else:
#         print("No luck!")


# print(apply(1,3,5,operator="*"))



def print_kwargs(**kwargs):
    print(kwargs)



def print_nicely(**kwargs):

    print_kwargs(**kwargs)

    for arg,value in kwargs.items():
        print(f'{arg}: {value}')



print_nicely(name="booster",age=25)