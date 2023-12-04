import time
import ttkbootstrap as ttk
from settings import WIDTH, HEIGHT
from widgets import ClockFrame, AlarmClockPanel, AddAlarmClock, AlarmsFrame

try:
    from ctypes import windll, byref, sizeof, c_int
except ImportError:
    pass


class App(ttk.Window):
    def __init__(self):
        super().__init__(themename = 'darkly')
        self.bind('<Alt-s>', lambda even: self.destroy())
        self.set_geometry(height = HEIGHT, width = WIDTH)
        self.title('')
        self.set_icon(path_image = 'media/empty.ico')
        self.set_title_color()
        
        # set data
        
        self.hour_int = ttk.IntVar(value = 0)
        self.minute_int = ttk.IntVar(value = 0)
        
        # create widgets
        self.clock_frame = ClockFrame(self)
        self.alarm_panel = AlarmClockPanel(self)
        self.add_alarm_clock_button = AddAlarmClock(self, button_function = self.add_alarms)
        
        # add the top level
        self.top_level = TopLevel(
                parent = self,
                hour_int = self.hour_int,
                minute_int = self.minute_int,
                ok_function = self.ok_button,
                cancel_function = self.cancel_button
                )
        
        # set layout for widgets(place method)
        
        self.clock_frame.place(
                relx = 0,
                rely = 0,
                relwidth = 1,
                relheight = 0.3,
                anchor = 'nw'
                )
        self.alarm_panel.place(
                relx = 0,
                rely = 0.3,
                relwidth = 1,
                relheight = 0.6,
                anchor = 'nw'
                )
        self.add_alarm_clock_button.place(
                relx = 0.5,
                rely = 0.95,
                anchor = 'center'
                )
        
        # run the window
        self.mainloop()
    
    def set_icon(self, path_image):
        try:
            self.iconbitmap(path_image)
        except Exception:
            pass
    
    def set_geometry(self, width, height):
        top = int(self.winfo_screenheight() / 2) - int(height / 2)
        left = int(self.winfo_screenwidth() / 2) - int(width / 2)
        self.geometry(f'{width}x{height}+{left}+{top}')
    
    def set_title_color(self):
        try:
            HWND: int = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE: int = 35
            color: int = 0x00EEEEEE
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(color)), sizeof(c_int))
        
        except Exception:
            pass
    
    def ok_button(self):
        if self.hour_int.get() or self.minute_int.get() != 0:
            
            hour, minute = self.hour_int.get(), self.minute_int.get()
            hour_str = str(hour) if hour >= 10 else f'0{hour}'
            minutes_str = str(minute) if minute >= 10 else f'0{minute}'
            
            text_label = f'{hour_str}:{minutes_str}'
            labels = AlarmsFrame(parent = self.alarm_panel, text = text_label)
            
            self.alarm_panel.add_alarm(labels)
    
    def cancel_button(self):
        
        self.hour_int.set(value = 0)
        self.minute_int.set(value = 0)
        self.destroy()
        print(self.hour_int.get())
    
    def add_alarms(self):
        labels = AlarmsFrame(self.alarm_panel, )
        self.alarm_panel.add_alarm(labels)


class TopLevel(ttk.Toplevel):
    def __init__(self, parent, hour_int, minute_int, ok_function, cancel_function):
        super().__init__(master = parent)
        
        # set attributes
        
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('Clock')
        self.set_geometry(width = 300, height = 300)
        
        # set data
        self.hour_int = hour_int
        self.minute_int = minute_int
        
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
                arrowsize = 30,
                )
        
        # create widgets
        
        self.hour_spin = ttk.Spinbox(
                master = self,
                textvariable = self.hour_int,
                font = ('Helvetica', 20, 'bold'),
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
                command = ok_function
                
                )
        self.cancel_label = ttk.Button(
                master = self,
                text = 'Cancel',
                command = cancel_function,
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


if __name__ == '__main__':
    App()
