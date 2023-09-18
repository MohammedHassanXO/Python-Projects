"""
Create a function that takes a sentence and word and remove the word from the sentence
"""
sentence = input("Enter the sentence : ",)
Xword = input("Enter the word : ",)
def sent (sentence) :
    sentlist = sentence.split()
    sentlist.remove(Xword)
    print(" ".join(sentlist))
    return
sent(sentence)