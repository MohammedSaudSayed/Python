def accept():
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    return n1, n2

def add():
    a, b = accept()
    return a + b

def sub():
    a, b = accept()
    return a - b

def mul():
    a, b = accept()
    return a * b

def div():
    a, b = accept()
    return a / b

def sq():
    n1 = int(input("Enter a number: "))
    print(n1 * n1)

def cube():
    n1 = int(input("Enter a number: "))
    print(n1 * n1 * n1)

print("1. Add\n2. Sub\n3. Mul\n4. Div\n5. Sq\n6. Cube")

choice = int(input("Enter your Choice: "))
print("Your choice is ", choice)

if choice == 1:
    print(add())

elif choice == 2:
    print(sub())

elif choice == 3:
    print(mul())

elif choice == 4:
    print(div())

elif choice == 5:
    print(sq())

elif choice == 6:
    print(cube())