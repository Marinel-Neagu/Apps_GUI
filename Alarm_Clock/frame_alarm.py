import ttkbootstrap as ttk
import pygame


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent, text):
        super().__init__(master = parent, )
        
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
        self.add_days()
    
    def add_days(self):
        list_day = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
        for index, day in enumerate(list_day):
            self.day_label = DayButton(
                    parent = self,
                    day_name = day,
                    row = 1,
                    column = index,
                    )
    
    def set_alarm(self):
        
        if self.variable_checkbutton.get():
            print(f'alarm set at {self.time_str} on {self}')
    
    def delete_alarm(self):
        self.destroy()


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
