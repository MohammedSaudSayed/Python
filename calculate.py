import calculator as c

n1 = int(input("Enter Number 1: "))
n2 = int(input("Enter Number 2: "))

print("Addition", c.add(n1, n2))
print("Subtraction", c.subtract(n1, n2))
print("Multiplication", c.multiply(n1, n2))
print("Division", c.divide(n1, n2))
print("Square", c.square(n1))