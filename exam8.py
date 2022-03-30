# linear search in python

ls = [1, 2, 0, 4, 9, 6]

search = int(input("Enter Element to Search: "))

if search in ls:
    print('search element is present.')
else:
    print('Element not found')