from random import random

def doSomething():
    print("Saud")
    if (True):
        print("Sayed")

def fun():
    a = random() * 10
    return round(a)

# do something
rt = fun()

n = int(input("Enter a number: "))

if (rt == n):
    print("You won a lottery")
else:
    print("Better luck next time")

print("Lottery number was", rt)