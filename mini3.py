# Random Password Generator

import random

passlen = int(input('Please Enter the length of password: '))
# print('password length: ', passlen)

optionkeys = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<>'
p = ''.join(random.sample(optionkeys, passlen))
print('Your Password is: ', p)
