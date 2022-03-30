# wap to print a list containing factorials of first 10 numbers

l = []

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

for i in range(1, 11):
    l.append(factorial(i))

print(l)