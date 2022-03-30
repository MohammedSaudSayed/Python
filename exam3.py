# wap to accept 5 numbers from the user and print its sq and cube

number = []

for i in range(5):
    n = int(input('Enter a number: '))
    number.append(n)

for n in number:
    print(n, n**2, n**3)