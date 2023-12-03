from ttkbootstrap.scrolled import ScrolledFrame
import ttkbootstrap as ttk
import time


class ClockFrame(ttk.Frame):
    def __init__(self, parent, ):
        super().__init__(master = parent)
        # layout
        self.rowconfigure(0, weight = 1, uniform = 'a')
        self.rowconfigure(1, weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')
        
        # set data
        self.time_string = ttk.StringVar()
        self.date_string = ttk.StringVar()
        
        # set set style
        self.style = ttk.Style()
        self.style.configure(
                style = 'Time.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        self.style.configure(
                style = 'Data.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                )
        
        # set widgets
        
        self.label_time = ttk.Label(
                master = self,
                textvariable = self.time_string,
                style = 'Time.TLabel'
                )
        
        self.label_date = ttk.Label(
                master = self,
                textvariable = self.date_string,
                style = 'Data.TLabel'
                )
        
        # set layout
        
        self.label_time.grid(
                row = 0,
                column = 0,
                columnspan = 2,
                sticky = 'ns'
                )
        self.label_date.grid(
                row = 1,
                column = 0,
                columnspan = 2,
                sticky = 'n'
                )
        
        # logic
        self.update_time()
    
    def update_time(self):
        # set time and date format
        
        time_format = "%H:%M:%S"
        date_format = "%a %B %d"
        
        # update the time for every 1 second(using a recursion func)
        
        self.time_string.set(time.strftime(time_format))
        self.after(1000, self.update_time)
        self.date_string.set(time.strftime(date_format))


class AlarmClockPanel(ScrolledFrame):
    def __init__(self, parent):
        super().__init__(master = parent)
    
    def add_alarm(self, alarm):
        alarm.pack(expand = True, fill = 'both')


class AddAlarmClock(ttk.Frame):
    def __init__(self, parent, button_function):
        super().__init__(master = parent)
        
        # button
        self.button = ttk.Button(
                master = self,
                text = '+',
                command = button_function,
                style = 'Alarm.TButton',
                )
        self.button.pack(expand = True, fill = 'both')
        self.top_level = TimeChoser(self)


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master = parent)
        
        self.alarm = ttk.Label(master = self, text = 'haha')
        self.alarm.pack(expand = True, fill = 'both')


class TimeChoser(ttk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(master = parent)
        
        # set attributes
        
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('Clock')
        self.set_geometry(width = 300, height = 300)
        
        # set data
        self.hour_int = ttk.IntVar(value = 0)
        self.minute_int = ttk.IntVar(value = 0)
        
        # set style
        self.top_level_style = ttk.Style()
        
        self.top_level_style.configure(
                style = 'OK.TButton',
                font = ('Helvetica', 10, 'bold'),
                background = 'black',
                anchor = 'center'
                )
        
        self.top_level_style.configure(
                style = 'CANCEL.TButton',
                font = ('Helvetica', 10, 'bold'),
                background = 'red',
                anchor = 'center'
                
                )
        self.top_level_style.configure(
                style = 'PAUSE.TLabel',
                font = ('Helvetica', 30, 'bold'),
                anchor = 'center'
                
                )
        self.top_level_style.configure(
                style = 'TSpinbox',
                background = 'green',
                anchor = 'center',
                width = 2,
                arrowsize = 50,
                )
        
        # create widgets
        
        self.hour_spin = ttk.Spinbox(
                master = self,
                textvariable = self.hour_int,
                font = ('Helvetica', 90, 'bold'),
                from_ = 0,
                to = 23
                )
        self.first_label = ttk.Label(
                master = self,
                style = 'PAUSE.TLabel',
                text = ':'
                )
        
        self.minute_spin = ttk.Spinbox(
                master = self,
                textvariable = self.minute_int,
                font = ('Helvetica', 20, 'bold'),
                from_ = 0,
                to = 59,
                )
        
        self.ok_label = ttk.Button(
                master = self,
                text = 'OK',
                style = 'OK.TButton',
                command = self.ok_button
                
                )
        self.cancel_label = ttk.Button(
                master = self,
                text = 'Cancel',
                command = self.cancel_button,
                style = 'CANCEL.TButton',
                )
        
        # layout
        self.rowconfigure((0, 1, 2, 3), weight = 1, uniform = 'a')
        self.columnconfigure((0, 1, 2), weight = 1, uniform = 'a')
        
        # first row
        self.hour_spin.grid(row = 1, column = 0)
        self.first_label.grid(row = 1, column = 1)
        self.minute_spin.grid(row = 1, column = 2)
        
        # second row(the button)
        self.ok_label.grid(row = 2, column = 0, sticky = 'news')
        self.cancel_label.grid(row = 2, column = 2, sticky = 'news')
    
    def set_geometry(self, width, height):
        top = int(self.winfo_screenheight() / 2) - int(height / 2)
        left = int(self.winfo_screenwidth() / 2) - int(width / 2)
        self.geometry(f'{width}x{height}+{left}+{top}')
    
    def ok_button(self):
        
        if self.hour_int.get() or self.minute_int.get() != 0:
            self.destroy()
        else:
            print('Sorry')
    
    def cancel_button(self):
        
        self.hour_int.set(value = 0)
        self.minute_int.set(value = 0)
        self.destroy()
