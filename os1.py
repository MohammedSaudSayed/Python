# read from a file
# counted the number of words in the file

import os

f = open('content.txt', 'r')
content = f.read()
print(content)
f.close()

# how many words in that file ?
words = content.split()
print("Words in the file are: ", len(words))
