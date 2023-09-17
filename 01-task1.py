'''
Create a python function that takes 2 numbers x,y and prints 2 lists containing the odd and even numbers in
the x,y range
'''

def evenodd() :
    evenlist = []
    oddlist = []
    x, y = map(int, input().split())

    for _ in range(x, y):
        if _%2 == 0 :
            evenlist.append(_)
        elif _%2 != 0 :
            oddlist.append(_)
            
    print("The even list ",evenlist)
    print("The odd list ",oddlist)
    return 
evenodd()