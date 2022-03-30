import os

f = open('content.txt', 'r')
content = f.read()
'''print(content)
f.close()'''

# how many words in that file ?
words = content.split()
print("Words in the file are: ", len(words))

wordsStartingwithA = []

for w in words:
    if w[0] == 'a' or w[0] == 'A' or w[0] == 'e' or w[0] == 'i' or w[0] == 'o' or w[0] == 'u':
        if w not in wordsStartingwithA:
            wordsStartingwithA.append(w)

print("Words Starting with a / A or vowels are: ", wordsStartingwithA)