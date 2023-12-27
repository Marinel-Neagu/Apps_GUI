import ttkbootstrap as ttk
import pygame
from time import sleep
import datetime
from threading import Thread


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent, text):
        super().__init__(master = parent, )
        
        # set grid layout
        
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(0, 7)), weight = 1, uniform = 'a')
        
        #  set data
        
        self.day_label = list(range(7))
        self.days_on = list()
        self.time_str = text
        self.variable_checkbutton = ttk.BooleanVar()
        
        # set widgets
        
        self.time_label = ttk.Label(
                master = self,
                text = self.time_str,
                )
        
        self.checkbutton = ttk.Checkbutton(
                master = self,
                variable = self.variable_checkbutton,
                command = self.set_alarm
                )
        
        self.delete_button = ttk.Button(
                master = self,
                text = 'Delete alarm',
                command = self.delete_alarm
                )
        
        # set layout
        self.time_label.grid(row = 0, column = 0, sticky = 'news')
        self.checkbutton.grid(row = 0, column = 5, sticky = 'news ')
        self.delete_button.grid(row = 0, column = 6, sticky = 'news')
        
        # add the layer of day
        list_day = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat',)
        
        for index, day in enumerate(list_day):
            self.day_label[index] = DayButton(
                    parent = self,
                    day_name = day,
                    row = 1,
                    column = index,
                    )
    
    def set_alarm(self):
        
        self.select_days()
        day = ", ".join(self.days_on)
        
        if self.variable_checkbutton.get():
            
            print(f'The alarm is set at: {self.time_str} on {day}')
            Thread(target = self.start_alarm, args = (self.time_str, day)).start()
        
        else:
            print(f'The alarm is off: {self.time_str} on {", ".join(self.days_on)}')
    
    def delete_alarm(self):
        self.destroy()
    
    def select_days(self):
        
        self.days_on.clear()
        for i in range(7):
            if not self.day_label[i].state.get():
                self.days_on.append(self.day_label[i]['text'])
    
    def start_alarm(self, time, day):
        hour = time.split(':')[0]
        minutes = time.split(':')[1]
        
        day_selected = day
        today = datetime.datetime.now().strftime('%a')
        print(today)
        
        total_second = 3600 * int(hour) + 60 * int(minutes)
        counter = 0
        
        if day_selected == today:
            print('alarm is clocking')
            while True:
                if counter <= total_second:
                    sleep(1)
                    counter += 1
                    print('Tic Tac:', counter)
                else:
                    print('Sound on is over')
                    break


class DayButton(ttk.Label):
    def __init__(self, parent, day_name, row, column):
        super().__init__(
                master = parent,
                text = day_name,
                background = 'green',
                )
        self.state = ttk.BooleanVar(value = True)
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                padx = 2,
                pady = 2
                )
        self.bind('<Enter>', self.enter_alarm)
        self.bind('<Leave>', self.leave_alarm)
        self.bind('<Button-1>', self.select_alarm)
    
    def enter_alarm(self, event = None):
        if self.state.get():
            self.configure(background = 'blue')
    
    def leave_alarm(self, event = None):
        if self.state.get():
            self.configure(background = 'green')
    
    def select_alarm(self, event = None):
        if self.state.get():
            self.configure(background = 'red')
            self.state.set(False)
        
        else:
            self.configure(background = 'green')
            self.state.set(True)
