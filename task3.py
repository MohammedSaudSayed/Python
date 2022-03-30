# reverse a list of names given by the user and print it

names = []

for i in range(3):
    str = input("Enter a name: ")
    names.append(str)

print(names)
names.reverse()
print(names)