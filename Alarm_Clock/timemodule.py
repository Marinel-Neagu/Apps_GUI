import time
import datetime
import threading

# dummy_date = 'Thu,21,22'
# date = dummy_date.split(',')
# day = date[0]
# hour = date[1]
# minutes = date[2]
# total_time = 3600 * int(hour) + 60 * int(minutes)
#
# while True:
#     initial_day = time.strftime('%a')
#     time_now = datetime.datetime.now()
#     initial_hour = time_now.hour
#     initial_minutes = time_now.minute
#     initial_second = time_now.second
#     initial_total_time = 3600 * initial_hour + 60 * initial_minutes + initial_second
#     if day == initial_day:
#         if initial_total_time <= total_time:
#             time.sleep(1)
#             print(f'{initial_hour}:{initial_minutes}:{time_now.second}')
#         else:
#             print('The alarm is done')
#             break
#     else:
#         break

event = threading.Event()

if event.is_set():
    print('good job')
else:
    print('bad job')
