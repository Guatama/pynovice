__author__ = 'Flatline01'
# That programm simulates the roll of two dice and display the result (sum of points).

print("With this program you throw two dice!")

# The random number generator throws two dice
while True:
    from random import randint
    dice11 = randint(1, 6)
    dice12 = randint(1, 6)
    result1 = dice11 + dice12

    print("--------------------------")
    print("First Dice:", dice11, "\t\tSecond Dice:", dice12, "\n\t\tYour points:", result1)


# The interface to end the program
    answer1 = ["no", "n", "quit", "bye", "exit"]
    choose = str(input("\nWant to continue? (enter/no)"))

    # Does the case insensitive
    choose = choose.lower()
    if choose in answer1:
        break
