import ttkbootstrap as ttk
import time
import pygame


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent, text):
        super().__init__(master = parent)
        
        # set grid layout
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(0, 7)), weight = 1, uniform = 'a')
        
        #  set data
        self.time_str = text
        self.variable_checkbutton = ttk.BooleanVar()
        self.days_on = list()
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
        # set layout
        self.time_label.grid(row = 0, column = 0, sticky = 'news')
        self.checkbutton.grid(row = 0, column = 6, sticky = 'news ')
        # add the layer of day
        self.add_days()
    
    def add_days(self):
        list_day = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
        for index, day in enumerate(list_day):
            self.day_label = DayButton(
                    parent = self,
                    day_name = day,
                    row = 1,
                    column = index,
                    function = self.select_alarm
                    )
    
    def set_alarm(self):
        
        if self.variable_checkbutton.get():
            print(f'alarm set at {self.time_str} on {self}')
        
        else:
            print('Is bad')
    
    def select_alarm(self, event = None):
        self.day_label.configure(background = 'red')
    
    def unselect_alarm(self, event = None):
        self.day_label.configure(background = 'green')


class DayButton(ttk.Label):
    def __init__(self, parent, day_name, row, column, function):
        super().__init__(
                master = parent,
                text = day_name,
                background = 'green',
                )
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                padx = 2,
                pady = 2
                )
        
        self.bind('<Button>', function(even = None))
