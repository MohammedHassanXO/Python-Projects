"""
Get the names that contains 2 or more ‘a’ letter using [normal list - list comprehension - functional programming]
"""

Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal list
modnames = []
count = 0 
for x in Names :
    count = len(x)
    modnames.append(count)
print(modnames)
    

# list comprehension
modnames2 = [len(x) for x in Names]
print(modnames2)

# functional programming
def count(Names) :
    count = 0 
    modnames3 = []
    for x in Names :
        count = len(x)
        modnames3.append(count)
    return modnames3
result = count(Names)
print(result)