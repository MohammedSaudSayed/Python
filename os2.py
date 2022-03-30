import os

str = input('Enter a Sentence: ')
print(str)

f = open('pontent.txt', 'a')  # r -> read   w -> write  a -> append
for s in str:
    f.write(str)

f.write(' ')

f.close()