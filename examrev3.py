# wap to accept 5 numbers from the user and print its sq and cube

numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

for num in numbers:
    print(num, num**2, num**3)