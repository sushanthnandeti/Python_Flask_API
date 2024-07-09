mydict = {"booster": 28, "pandu" : 20, "chittt": 55}


mylist = list(mydict.items())
print(mylist)


for name,age in mydict.items():
    print(f'{name} age is {age}')