## Program 1 - Division

def division(dividend, divisor):

    if divisor == 0: 
        raise ZeroDivisionError('This is not divisible by zero')
    
    return dividend/divisor 



def calculate(*values, operator):
    return operator(*values)


result = calculate(15,12,operator=division)
print(result)


## Program 2 - Search 

def search(sequence, expected, finder):
    
    for item in sequence:
        if finder(item) == expected:
            return item 
        
    raise RuntimeError('This name does not exist')


friends = [
    {"name": "Sushanth", "age" : "26"},
    {"name": "Susheel", "age" : "20"},
    ]


def get_my_friend(friends): 
    return friends["name"]

print(search(friends,"Susheel",get_my_friend(friends) ))



