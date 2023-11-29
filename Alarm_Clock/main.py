import customtkinter as ctk
from settings import WIDTH, HEIGHT
from widgets import ClockFrame, AlarmClock, AddAlarmClock

try:
    from ctypes import windll, byref, sizeof, c_int
except ImportError:
    pass


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bind('<Alt-s>', lambda even: self.destroy())
        self.set_geometry(height = HEIGHT, width = WIDTH)
        self.title('')
        self.set_icon('images/empty.ico')
        self.set_title_color()
        
        # set layout
        self.rowconfigure((0, 1, 2), weight = 1, uniform = 'a')
        self.columnconfigure(0, weight = 1, uniform = 'a')
        
        # set widgets
        self.create_widgets()
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
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            color = 0
            
        except Exception:
            print('Error in setting')
    
    def create_widgets(self):
        # create widgets
        clock_frame = ClockFrame(self)
        alarm_frame = AlarmClock(self)
        add_alarm_clock_frame = AddAlarmClock(self)
        
        # set layout for widgets
        clock_frame.grid(row = 0, column = 0, sticky = 'nsew')
        alarm_frame.grid(row = 1, column = 0, sticky = 'nsew')
        add_alarm_clock_frame.grid(row = 2, column = 0, sticky = 'esw')


if __name__ == '__main__':
    App()
