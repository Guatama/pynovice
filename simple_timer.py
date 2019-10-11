import datetime
import time
import os


def timer(minute :int):
    counter = 0
    timer_time = minute * 60
    second_point = ""
    while counter <= timer_time:
        os.system("cls")

        if counter % 2 == 0:
            second_point = "*"
        else:
            second_point = ""

        now = datetime.datetime.today().time()
        print("{}:{}:{}{}".format(now.hour, now.minute, now.second, second_point))

        counter += 1
        time.sleep(1)


def Main():
    min_test = input("Minute: ")
    timer(int(min_test))


if __name__ == "__main__":
    Main()
