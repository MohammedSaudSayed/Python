students = {"1": "Saud", "2": "Danish", "3": "Shahnawaz", "4": "Husain", "5": "Faiz"}

def add(rollno, name):
    students[rollno] = name

def search(rollno):
    if rollno in students:
        print(rollno, "is there")
    else:
        print("Student not found")

def delete(rollno):
    if rollno in students:
        del rollno
    else:
        print("Not found")

def display():
    for k,v in students.items():
        print(k,v)

def update(rollno, name):
    if rollno in students:
        add(rollno, name)
    else:
        print("Not found")

add("6", "Yash")
display()

search("5")
display()

delete("6")
display()

update("5","Arfat")
display()
