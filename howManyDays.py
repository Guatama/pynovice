__author__ = 'Flatline01'
# The program calculates the number of days from today's date to the date entered by the user
import datetime

def date2day(date_for_deadline): 
    deadlineDate = datetime.datetime.strptime(date_for_deadline, "%d/%m/%Y").date()
    time_between = deadlineDate - datetime.date.today()
    numDays = time_between.days
    return numDays

if __name__ == '__main__':
        
    print("Here you can calculate how many\ndays are left until a certain date.")

    your_date = date2day(input("\nEnter date of event (DD/MM/YY): "))

    print("\nToday is " + datetime.date.today().strftime('%d %B, %Y'))
    if your_date > 0:
        print("Before the event " + str(your_date) + " days left.")

    elif your_date == 0:
        print("This event is Today!")

    else:
        your_date *= -1
        print("After the event, " + str(your_date) + " days have passed.")

# TODO: add support "negative" date (how much days went after birth date for example) DONE
# TODO: add function for calculation parts and simplify the code