# linear search in python

ls = [1, 5, 7, 9, 25, 6]

search = int(input("Enter element to search: "))

if search in ls:
    print("Search element is present")
else:
    print("Element not found")