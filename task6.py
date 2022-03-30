# wap to accept 10 names from the user and store the names in the list only if the name has more than 6 characters.

words = []
for i in range(10):
    str = input("Enter words: ")
    if(len(str) >= 6):
        words.append(str)

print(words)