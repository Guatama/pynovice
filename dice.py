__author__ = 'Flatline01'
# import random
import numpy as np

# Code simulates the roll of two dice and display the result (sum of points).
if __name__ == '__main__':
    answer = ["no", "n", "quit", "bye", "exit", "q"]
    while True:
        # dice1 = random.randint(1, 6)
        # dice2 = random.randint(1, 6)
        dice1, dice2 = np.random.randint(1, 7, 2)
        result = dice1 + dice2

        print("\n\n--------------------------")
        print(f"Dice: {dice1}\t\tDice: {dice2}\nYour points: {result}")
        print("--------------------------")

        choose = str(input("Want to continue? (enter/no)")).lower()
        if choose in answer or choose.isdigit():
            break
