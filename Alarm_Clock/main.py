import customtkinter as ctk
from settings import WIDTH, HEIGHT
from widgets import ClockFrame, AlarmClockPanel, AddAlarmClock

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
        self.set_icon(path_image = 'media/empty.ico')
        self.set_title_color()
        
        # set widgets
        self.create_widgets()
        
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
    
    def create_widgets(self):
        # create widgets
        clock_frame = ClockFrame(self)
        alarm_panel = AlarmClockPanel(self)
        add_alarm_clock_button = AddAlarmClock(self)
        
        # set layout for widgets(place method)
        
        clock_frame.place(
                relx = 0,
                rely = 0,
                relwidth = 1,
                relheight = 0.3,
                anchor = 'nw'
                )
        alarm_panel.place(
                relx = 0,
                rely = 0.3,
                relwidth = 1,
                relheight = 0.6,
                anchor = 'nw'
                )
        add_alarm_clock_button.place(
                relx = 0.5,
                rely = 0.95,
                anchor = 'center'
                )


if __name__ == '__main__':
    App()
