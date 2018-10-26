__author__ = 'Flatline01'
# The program calculates the number of days from today's date to the date entered by the user
import datetime

currentDate = datetime.date.today()

print("Here you can calculate how many\ndays are left until a certain date.")

deadlineDate = datetime.datetime.strptime(input("\nEnter date of event (DD/MM/YY): "), "%d/%m/%Y").date()
time_between = deadlineDate - currentDate
numDays = time_between.days

print("\nToday is " + currentDate.strftime('%d %B, %Y'))
if numDays > 0:
    print("Before the event " + str(numDays) + " days left.")

elif numDays == 0:
    print("This event is Today!")

else:
    numDays *= -1
    print("After the event, " + str(numDays) + " days have passed.")


# TODO: add support "negative" date (how much days went after birth date for example) DONE
# TODO: add function for calculation parts and simplify the code