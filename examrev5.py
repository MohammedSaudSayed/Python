# Dice Roll Stimulator

import random as r

while True:
    print("1. Roll the Dice\n2. Quit")
    choice = int(input("Enter a number: "))
    if choice == 1:
        print("Rolling the dice....")
        print(r.randint(1,6))

    else:
        break
