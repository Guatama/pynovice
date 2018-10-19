"""
The game of guessing the number in the specified range, with the implementation of the binary search algorithm.
"""
__author__ = 'Flatline01'
import math

x_range = 1
y_range = 100
last_guess_number = 0

effort_number = 0
efforts = math.log(y_range, 2)
print(f"I will guess the number in no more than {round(efforts)} attempts.")

while x_range <= y_range:
    # last_guess_number = (x_range + y_range) / 2 - this is formula for binary search too
    last_guess_number = x_range + (y_range - x_range) / 2
    print(f"I guess it's {round(last_guess_number)}?")
    answer = input("Answer: ")
    
    if effort_number > efforts:
        print(f"Correct answer is {last_guess_number}! Don't fool me!")
        break

    if answer.lower() == "yes":
        print(f"Correct! It's {round(last_guess_number)}")
        break
        
    elif answer.lower() == "more":
        effort_number += 1
        print(f"It's effort number {effort_number}. Try again!")
        x_range = last_guess_number

    elif answer.lower() == "less":
        effort_number += 1
        print(f"It's effort number {effort_number}. Try again!")
        y_range = last_guess_number

