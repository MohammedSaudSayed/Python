# wap to print a list containing factorials of first 10 numbers

l = []

for i in range(1, 11):
    fact = 1
    for j in range(1, i+1):
        fact = fact * j
    l.append(fact)

print(l)