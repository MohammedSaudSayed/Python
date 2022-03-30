# wap to accept 5 numbers from the user and print its sq and cube using function

number = []

def find(n):
    print(n, n**2, n**3)


for i in range(5):
    num = int(input('Enter a number: '))
    number.append(num)

for n in number:
    find(n)