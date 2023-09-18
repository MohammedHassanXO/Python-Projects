"""
Create a function that takes x,y and prints all the number that can be divide by y from x to 100
"""

def divi() :
    list = []
    x, y = map(int , input().split())

    for _ in range(x, 100):
        if _%y == 0 :
            list.append(_)
    print("The list ",list)
    return
divi()