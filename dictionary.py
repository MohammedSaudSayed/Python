students = {1: 'Saud', 2: 'Sam', 3: 'Rock', 4: 'John', 5: 'Dom'}

print(students)
print(students[1])

students[1] = "Aiman"
print(students)

students[6] = "Jasmine"
print(students)

del students[6]
print(students)

# for s in students:
#     print(s, students[s])

for k, v, in students.items():
    print(k, v)   # k -> Keys, v -> Values