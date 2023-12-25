# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print('You eat breakfast')
#
#
# def drink_coffe():
#     time.sleep(4)
#     print('You drank coffe')
#
#
# def study():
#     time.sleep(5)
#     print('You finished study')
#
#
# x = threading.Thread(target = eat_breakfast, args = ())
# x.start()
# y = threading.Thread(target = drink_coffe, args = ())
# y.start()
# z = threading.Thread(target = study, args = ())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# print(threading.active_count())
# print(threading.enumerate())

# from multiprocessing import Process, cpu_count
# import time
#
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
#
# def main():
#     print(cpu_count())
#     a = Process(target = counter, args = (25000000,))
#     a.start()
#
#     b = Process(target = counter, args = (25000000,))
#     b.start()
#
#     c = Process(target = counter, args = (25000000,))
#     c.start()
#
#     d = Process(target = counter, args = (25000000,))
#     d.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#
#     print('finished in :', time.perf_counter(), ' seconds')
#
#
# if __name__ == '__main__':
#     main()

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print('logged in for: ', count, ' second')


x = threading.Thread(target = timer, daemon = True)
# x.setDaemon(True)
print(x.isDaemon())
x.start()
answer = input('Do you wish to exit?')
