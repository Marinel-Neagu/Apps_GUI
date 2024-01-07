import datetime
import time
from threading import Event


def get_date_now() -> int:
    time_now = datetime.datetime.now()
    initial_hour = time_now.hour
    initial_minutes = time_now.minute
    initial_second = time_now.second
    initial_time = 3600 * initial_hour + 60 * initial_minutes + initial_second
    
    return initial_time


class AlarmClock:
    def __init__(self, clock, event, days):
        self.clock = clock
        self.event = event
        self.days = days
        self.total_time = self.user_time()
        
        self.start_alarm()
    
    def user_time(self):
        hour_mim = self.clock.split(':')
        hour = int(hour_mim[0])
        minutes = int(hour_mim[1])
        
        return 3600 * hour + 60 * minutes
    
    def check_day(self):
        initial_day = time.strftime('%a')
        for day in self.days:
            if day == initial_day:
                self.days.remove(day)
    
    def counter_timer(self):
        initial_time = get_date_now()
        if initial_time >= self.total_time:
            time.sleep(60)
            self.start_alarm()
        else:
            time.sleep(1)
    
    def start_alarm(self):
        while not self.event.is_set():
            if len(self.days) == 0:
                break
            else:
                self.check_day()
                while not self.event.is_set():
                    self.counter_timer()
