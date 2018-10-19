__author__ = 'Flatline01'
# The program calculates the number of days from today's date to the date entered by the user
import datetime

currentDate = datetime.date.today()

print("Here you can calculate how many\ndays are left until a certain date.")

deadlineDate = datetime.datetime.strptime(input("\nEnter date of event (DD/MM/YY): "), "%d/%m/%Y").date()
numDays = deadlineDate - currentDate

print("\nToday is " + currentDate.strftime('%d %B, %Y'))
print("Before the event " + str(numDays.days) + " days left.")

# TODO: add support "negative" date (how much days went after birth date for example)