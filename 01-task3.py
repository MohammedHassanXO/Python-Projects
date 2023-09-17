"""
Create a python function that takes 2 numbers x, y and prints the multiplication table from x to y
"""

def mult() :
    x, y = map(int, input().split())

    for num in range(x, y + 1):
        print(f"The multiplication table of {num}:")
        for i in range(1, 13):
            result = num * i
            print(f"{num} x {i} = {result}")
        
    return
mult()