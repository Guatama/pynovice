__author__ = 'Flatline01'
import datetime

choosenDate = datetime.date.today()
answer1 = ["no", "n"]
answer2 = ["yes", "y"]

print("This program calculate the deadline date,\nif the user enters number of days before that.\n")
choose = str(input("Do you want to enter a specific date? (Y/N) "))

# Does the case insensitive
choose = choose.lower()

if choose in answer1:
    print("\nToday is " + choosenDate.strftime("%d %B, %Y"))
elif choose in answer2:
    inputDate = input("\nEnter the start date (DD/MM/YYYY): ")
    choosenDate = datetime.datetime.strptime(inputDate, "%d/%m/%Y").date()

passingDay = datetime.timedelta(days = int(input("Enter the number of days: ")))
deadlineDay = choosenDate + passingDay
print("\nDeadline will come  " + deadlineDay.strftime("%d %B, %Y"))
