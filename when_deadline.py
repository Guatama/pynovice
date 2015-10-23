__author__ = 'Flatline01'
import datetime

choosenDate = datetime.date.today()
answerN = ["no", "n"]
answerY = ["yes", "y"]
repeatQuestion = False

print("This program calculate the deadline date,\nif the user enters number of days before that.\n")

while repeatQuestion == False:
    choose = str(input("Do you want to enter a specific date? (Y/N) "))

    # Does the case insensitive
    choose = choose.lower()

    if choose in answerN:
        repeatQuestion = True
        print("\nToday is " + choosenDate.strftime("%d %B, %Y"))

    elif choose in answerY:
        repeatQuestion = True
        inputDate = input("\nEnter the start date (DD/MM/YYYY): ")
        choosenDate = datetime.datetime.strptime(inputDate, "%d/%m/%Y").date()

passingDay = datetime.timedelta(days = int(input("Enter the number of days: ")))
deadlineDay = choosenDate + passingDay
print("\nDeadline will come  " + deadlineDay.strftime("%d %B, %Y"))
