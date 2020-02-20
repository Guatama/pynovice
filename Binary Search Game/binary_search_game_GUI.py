"""
The game of guessing the number in the specified range, with the implementation of the binary search algorithm.
"""
__author__ = 'Flatline01'
from math import log
import PySimpleGUI as sg

# last_guess_number = 1
x_range = 1
y_range = 100

# Start window
layout_one = [ [sg.Text('Choose a range of numbers and make a number.')],
           [sg.Text('From '), sg.InputText(do_not_clear=True), sg.Text('to '), sg.InputText(do_not_clear=True)],      
           [sg.Button('Start Game')] ]

window = sg.Window('Binary Search Game').Layout(layout_one)
while True:
    button, range = window.Read()
    x_range, y_range = range
    x_range = int(x_range)
    y_range = int(y_range)

    if button == 'Start Game' and x_range < y_range:
        break
window.Close()

# Second window
effort_number = 1
efforts = log(y_range, 2)
last_guess_number = x_range + (y_range - x_range) / 2

layout_two = [[sg.Text(f'{round(last_guess_number)}', key='output'), sg.Text('is your number?')],
           [sg.Button('Less'), sg.Button('YES'), sg.Button('More')],
           [sg.Text(f"{effort_number}", key="effort_number"), sg.Text("|"), sg.Text(f"{round(efforts)}")], 
           [sg.ProgressBar(efforts, orientation='h', size=(20, 20), key='progbar')]
]

window2 = sg.Window('Binary Search Game').Layout(layout_two)
while True:
    event, values = window2.Read()

    if event is not None:
        if event == "YES":
            break
        if event == "More":
            effort_number += 1
            x_range = last_guess_number
        if event == "Less":
            effort_number += 1
            y_range = last_guess_number

        last_guess_number = x_range + (y_range - x_range) / 2
        window2.FindElement('output').Update(round(last_guess_number))
        window2.FindElement('effort_number').Update(effort_number)
        window2.FindElement('progbar').UpdateBar(effort_number)

    else:
        break
window2.Close()



# print(f"I will guess the number in no more than {round(efforts)} attempts.")
# while x_range <= y_range:
#     # last_guess_number = (x_range + y_range) / 2 - this is formula for binary search too
#     last_guess_number = x_range + (y_range - x_range) / 2
#     print(f"I guess it's {round(last_guess_number)}?")
#     answer = input("Answer: ")
    
#     if effort_number > efforts:
#         print(f"Correct answer is {last_guess_number}! Don't fool me!")
#         break

#     if answer.lower() == "yes":
#         print(f"Correct! It's {round(last_guess_number)}")
#         break
        
#     elif answer.lower() == "more":
#         effort_number += 1
#         print(f"It's effort number {effort_number}. Try again!")
#         x_range = last_guess_number

#     elif answer.lower() == "less":
#         effort_number += 1
#         print(f"It's effort number {effort_number}. Try again!")
#         y_range = last_guess_number


