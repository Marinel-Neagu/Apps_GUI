import customtkinter as ctk
import time


class ClockFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
        # layout
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')
        # set data
        self.time_string = ctk.StringVar()
        self.date_string = ctk.StringVar()
        
        # set font for labels
        time_font = ctk.CTkFont(
                family = 'Helvetica',
                size = 60,
                weight = "bold",
                )
        
        date_font = ctk.CTkFont(
                family = 'Helvetica',
                size = 25,
                weight = "bold",
                )
        # set widgets
        
        self.label_time = ctk.CTkLabel(
                master = self,
                textvariable = self.time_string,
                font = time_font,
                anchor = 'center'
                )
        
        self.label_date = ctk.CTkLabel(
                master = self,
                textvariable = self.date_string,
                anchor = 'center',
                font = date_font,
                )
        
        self.label_time.grid(row = 0, column = 0, columnspan = 2, sticky = 'ns')
        self.label_date.grid(row = 1, column = 0, columnspan = 2, sticky = 'n')
        
        # logic
        self.update_time()
    
    def update_time(self):
        time_format = "%H:%M:%S"
        date_format = "%a %B %d"
        
        self.time_string.set(time.strftime(time_format))
        self.after(1000, self.update_time)
        self.date_string.set(time.strftime(date_format))


class AlarmClock(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = 'red')
        


class AddAlarmClock(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master = parent, fg_color = 'blue')
