"""
Using the names list above create a python code that :
1. Transform all names to uppercase using [normal list - list comprehension - functional programming]
"""
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# Normal list
modnames = []
for x in Names :
    modnames.append(x.upper())
print(modnames)

# list comprehension
modnames2 = [x.upper() for x in Names]
print(modnames2)

# functional programming
def changcase(x) :
    return x.upper()
modnames3 = list(map(changcase, Names))
print(modnames3)