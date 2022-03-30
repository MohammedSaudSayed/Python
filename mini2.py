# Guess the number game - MATKA

import random as r

number = r.randint(1,10)

for i in range(0,3):
    guess = int(input('Guess the Number: '))
    if guess == number:
        print('You Won')
        break

    else:
        print('Wrong Guess')
        if i == 2:
            print('You Lost. Play Again')
            print('The number was', number)
