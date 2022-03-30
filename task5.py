# wap to accept words (min 10) from the user and store it in the list only if the words start with the letter 'a' or 'A'

words = []
for i in range(10):
    str = input("Enter words: ")
    if(str[0] == 'a' or str[0] == 'A'):
        words.append(str)

print(words)