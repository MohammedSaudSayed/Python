# wap to accept list of numbers from the user and display only even numbers from the list

numbers = []
for i in range(10):
    num = int(input("Enter numbers: "))
    numbers.append(num)

for i in range(5):
    if numbers[i] % 2 == 0:
        print(numbers[i])