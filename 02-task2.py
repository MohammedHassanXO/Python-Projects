"""
Get the names that contains ‘a’ in a list using [normal list - list comprehension - functional programming]
"""
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal list
modnames = []
for x in Names :
    index = x.find("a")
    if index >= 0 :
        modnames.append(x)
print(modnames)

# list comprehension
modnames2 = [x for x in Names if x.find("a")>= 0 ]
print(modnames2)

# functional programming
def finder(Names) :
    modnames3 = []
    for x in Names :
        if 'a' in x :
            modnames3.append(x)
    return modnames3
result = finder(Names)
print(result)