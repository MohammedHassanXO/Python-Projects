"""
Unpack the list in
"""
Names = ['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

# a,b , a= the first index , b = rest of the list
a , *b =  Names
print(a)
print(b)
print( )
# a = the first index , b = the last index
x, *c, y = Names
print(x)
print(y)
print( )
# a = the first index , b = the second index
f, g, *h = Names
print(f)
print(g)