# wap to accept 5 student from the teacher and store it in a list
# Disply names starting from the letter 'A'

students = []

for i in range(5):
    name = input('Enter a name: ')
    students.append(name)

print('student starting with A or a are: ')
for s in students:
    if s[0] == 'A' or s[0] == 'a':
        print(s)

# print(students)