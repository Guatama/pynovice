from datetime import datetime
from time import sleep
from os import system
import platform


def timer(minute: int) -> None:
    counter = 0
    timer_time = minute * 60
    second_point = ""
    while counter <= timer_time:
        if platform.system() == 'Windows':
            system('cls')
        else:
            system('clear')

        second_point = "*" if counter % 2 else " "
        now = datetime.today().time()
        print("{:02}:{:02}:{:02}{}".format(now.hour, now.minute,
                                           now.second, second_point))
        counter += 1
        sleep(1)

    print("DONE! {} min. pass!".format(minute))


def main():
    min_test = input("Minute: ")
    timer(int(min_test))


if __name__ == "__main__":
    main()
