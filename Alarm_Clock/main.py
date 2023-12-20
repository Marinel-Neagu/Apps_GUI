from toplevel import TopLevel
import ttkbootstrap as ttk
from configuration import WIDTH, HEIGHT
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
        self.set_icon(path_image = 'media/image/empty.ico')
        self.set_title_color()
        
        # set data
        
        self.hour_int = ttk.IntVar(value = 0)
        self.minute_int = ttk.IntVar(value = 0)
        self.top_level = None
        
        # create widgets
        self.clock_frame = ClockFrame(self)
        self.alarm_panel = AlarmClockPanel(parent = self)
        self.button_top_level = AddAlarmClock(parent = self, button_function = self.start_top_level)
        
        # dummy alarm for testing
        
        alarm = AlarmsFrame(
                parent = self.alarm_panel,
                text = '12:00',
                )
        self.alarm_panel.add_alarm(alarm)
        
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
        self.button_top_level.place(
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
            color: int = 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(color)), sizeof(c_int))
        
        except Exception:
            pass
    
    def start_top_level(self):
        self.top_level = TopLevel(
                parent = self,
                hour_int = self.hour_int,
                minute_int = self.minute_int,
                ok_function = self.ok_button,
                cancel_function = self.cancel_button
                )
    
    def ok_button(self):
        if self.hour_int.get() or self.minute_int.get():
            
            hour, minute = self.hour_int.get(), self.minute_int.get()
            hour_str = str(hour) if hour >= 10 else f'0{hour}'
            minutes_str = str(minute) if minute >= 10 else f'0{minute}'
            
            text_label = f'{hour_str}:{minutes_str}'
            alarm_frame = AlarmsFrame(parent = self.alarm_panel, text = text_label)
            
            self.alarm_panel.add_alarm(alarm_frame)
            self.hour_int.set(value = 0)
            self.minute_int.set(value = 0)
            self.top_level.destroy()
    
    def cancel_button(self):
        
        self.hour_int.set(value = 0)
        self.minute_int.set(value = 0)
        self.top_level.destroy()


if __name__ == '__main__':
    App()
