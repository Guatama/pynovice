__author__ = 'Flatline01'
import datetime

def days2date(days, start_date = None):
    """
    Calculate the deadline date, if the user enters number of days before that.
    """

    if start_date:
        start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    else:
        start_date = datetime.date.today()

    pass_days = datetime.timedelta(days)
    date = start_date + pass_days

    return date.strftime("%d %B, %Y")


def date2days(date, start_date = None):
    """
    The function returns the number of days until a certain date
    By default: start_date == Today
    """
    if start_date:
        start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    else:
        start_date = datetime.date.today()

    date = datetime.datetime.strptime(date, "%d/%m/%Y").date()
    time_between = date - start_date

    return time_between.days


if __name__ == '__main__':  # Testing
    test_days = 30
    test_start = None
    test_date = "01/01/2020"
    test_result = days2date(test_days, test_start)
    
    print("Test sequence - started ...")
    print("-----------------------------")
    print("After {} will be that date: {}".format(test_days, test_result))
    print(days2date(356))
    print(days2date(356, "01/01/2018"))
    print(date2days(test_date))
    print(date2days(test_date, "01/01/2018"))
    print("-----------------------------")
    print("... Test sequence - DONE\n")

    print("Here you can calculate how many\ndays are left until a certain date.")
    your_date = date2days(input("\nEnter date of event (DD/MM/YY): "))
    print("\nToday is {}".format(datetime.date.today().strftime('%d %B, %Y')))

    if your_date > 0:
        print("Before the event {} days left.".format(your_date))
    elif your_date == 0:
        print("This event is Today!")
    else:
        print("After the event, {} days have passed.".format(your_date * -1))
