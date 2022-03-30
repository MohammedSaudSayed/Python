# wap to except 5 names from the user and store it in a list, later check if aiman is there in those numbers

names = []

for i in range(5):
    str = input("Enter Name: ")
    names.append(str)

print(names)
print("Aiman is there in the list: ", "Aiman" in names)
