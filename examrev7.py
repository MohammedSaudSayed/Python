# Random Password Generator

import random as r

passlen = int(input("Enter the length of password: "))

optionkeys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+<>?'

p = ''.join(r.sample(optionkeys, passlen))

print("Your password is", p)