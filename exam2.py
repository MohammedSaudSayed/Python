# wap to accept roll no and name of 5 students from teacher and print them

students = {}

for i in range(5):
    rollno = int(input("Enter Roll No: "))
    name = input('Enter a name: ')
    students[rollno] = name


print('RollNo', 'Name')
for k,v in students.items():
    print(k,v)