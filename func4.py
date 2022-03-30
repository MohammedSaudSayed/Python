# type 4 - with params and with return value

def add(n1, n2):
    return (n1 + n2)

print("Enter two numbers to add: ") 
num1= int(input('Enter first number: ')) 
num2= int(input('Enter second number: '))

ans = add(num1, num2) 
print('The sum of the two numbers is: ', ans)

print("The sum of the two numbers is: ",add(100, 200))