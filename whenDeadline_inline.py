__author__ = 'Flatline01'
import datetime, sys
days = int(sys.argv[1])
try:
    startDate = sys.argv[2]
except IndexError:
    startDate = None
    pass

if startDate:
    startDate = datetime.datetime.strptime(startDate, "%d/%m/%Y").date()
else:
   startDate = datetime.date.today()

passingDay = datetime.timedelta(days)
deadlineDay = startDate + passingDay
print(deadlineDay.strftime("%d %B, %Y"))

