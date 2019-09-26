__author__ = 'Flatline01'
from random import randint

# That programm simulates the roll of two dice and display the result (sum of points).
if __name__ == '__main__':
    answer = ["no", "n", "quit", "bye", "exit", "q"]
    while True:   
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        result = dice1 + dice2

        print("--------------------------")
        print(f"Dice: {dice1}\t\tDice: {dice1}\nYour points: {result}")
        print("--------------------------")

        choose = str(input("\nWant to continue? (enter/no)")).lower()
        if choose in answer or choose.isdigit():
            break