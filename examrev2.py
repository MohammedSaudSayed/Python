# wap to accept roll no and name of 5 students from teacher and print them

students = {}

for i in range(5):
    rollno = int(input("Enter roll no of a student: "))
    name = input("Enter name of a student: ")
    students[rollno] = name

print("RollNo & Name")

for k,v in students.items():
    print(k,v)