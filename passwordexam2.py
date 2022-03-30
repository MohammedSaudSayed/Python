import random as r

passlen = int(input("Enter the length of password: "))

optionkeys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+<>?:'

p = ''.join(r.sample(optionkeys, passlen))

print(p)