# MATKA - Guessing the Number

import random as r

num = r.randint(1,10)

for i in range(0,3):
    guess = int(input("Please Guess a Number: "))
    if guess == num:
        print(f"You Won\n with guess number!--{num}")
        break
    else:
        print("Wrong Guess")

if guess != num:
    print(f"You lost the game, and the number was", num )