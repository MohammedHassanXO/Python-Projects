"""
Create a function that takes a sentence and prints the sentence without duplicated words
"""

def sent() :
    stringlist = input().split()
    edlist = []

    for _ in stringlist:
        if (stringlist.count(_) >= 1 and ( _ not in edlist)) :
            edlist.append(_)

    print(' '.join(edlist))
    return
sent()