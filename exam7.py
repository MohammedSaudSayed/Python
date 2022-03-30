# Random Password Generator

import random as r

passlen = int(input('Please Enter the length of password: '))
# print('password length: ', passlen)

optionkeys = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?<>'
p = ''.join(r.sample(optionkeys, passlen))
print('Your Password is: ', p)
