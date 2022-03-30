# wap to accept 10 student from the teacher and store it in a list
# Disply names starting from the letter 'Z' or 'z'

students = []

for i in range(5):
    name = input("Enter a name: ")
    students.append(name)

print("Students whose number starts with Z or z are: ")
for s in students:
    if s[0] == 'z' or s[0] == 'Z':
        print(s)