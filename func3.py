# type 3 - no params and with return value

def add():
    print("Enter two numbers to add: ")

    num1 = int(input('Enter first number: ')) 
    num2= int(input('Enter second number: '))
    return (num1 + num2)

ans = add()
print('The sum of the two numbers is: ', ans)

# above done in one line
print('the sum of the two numbers is: ', add())