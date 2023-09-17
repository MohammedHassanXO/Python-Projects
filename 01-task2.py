"""
Create a python function that takes 2 numbers x,y and prints all the numbers between 1 and 100 than can
be divided on x,y
"""

def divi() :
    list = []
    x, y = map(int , input().split())

    for _ in range(1, 100):
        if _%x == 0 and _%y == 0 :
            list.append(_)
    print("The list ",list)
    return
divi()