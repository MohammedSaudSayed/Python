# MATKA - Guessing the Number

import random as r

num = r.randint(1,10)

for i in range(3):
    guess = int(input("Enter a number: "))
    if guess == num:
        print(f"You won with the guess number! {num}")
        break
    else:
        print("You Lost")

if guess != num:
    print(f"You lost the game and the number was", num)