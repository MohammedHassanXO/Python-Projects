"""
Create a function takes a sentence and a word and prints how many time the word used in the sentence
"""

sentence = input("Enter the sentence : ",)
Xword = input("Enter the word : ",)
def sent (sentence) :
    sentlist = sentence.split()
    print(sentlist.count(Xword))
    return
sent(sentence)