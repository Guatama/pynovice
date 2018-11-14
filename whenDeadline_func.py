__author__ = 'Flatline01'

def deadline_date(days, startDate = None):
    """
    This function calculate the deadline date, if the user enters number of days before that.
    """
    import datetime
    if startDate:
        startDate = datetime.datetime.strptime(startDate, "%d/%m/%Y").date()
    else:
        startDate = datetime.date.today()

    passingDay = datetime.timedelta(days)
    deadlineDay = startDate + passingDay
    return deadlineDay.strftime("%d %B, %Y")


if __name__ == '__main__':  # Testing
    test_days = 30
    test_start = None # or string "10/11/2018"
    test_result = deadline_date(test_days, test_start)
    print("Today is {}. After {} will be that date: {}".format(test_start, test_days, test_result))
    print(deadline_date(356))
    print(deadline_date(356, "01/01/2018"))
