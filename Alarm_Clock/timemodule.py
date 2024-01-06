import time
import datetime

list_weekday = ['Mon', 'Sat']


def func(list_day):
    while True:
        if len(list_day) == 0:
            print('The list is empty')
            break
        for day in list_day:
            if day == time.strftime('%a'):
                list_day.remove(day)


if __name__ == '__main__':
    func(list_weekday)
