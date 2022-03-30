# Dice Roll Stimulator

import random as r

while True:
    print('1. Roll the Dice\n2. Exit')
    choice = int(input('Please Enter your Choice: '))
    if choice == 1:
        print('Rolling the dice......')
        print(r.randint(1,6))
    
    else:
        break