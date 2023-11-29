import customtkinter as ctk
from settings import WIDTH, HEIGHT
from widgets import ClockFrame, AlarmClock


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bind('<Alt-s>', lambda even: self.destroy())
        self.set_geometry(height = HEIGHT, width = WIDTH)
        self.title('')
        self.set_icon('images/empty.ico')
        
        # set layout
        self.rowconfigure = ()
        self.columnconfigure = ()
        
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
    
    
    def create_widgets(self):
        # create widgets
        clock_frame = ClockFrame(self)
        alarm_frame = AlarmClock(self)
        
        # set layout for widgets
        clock_frame.pack(fill = 'both')
        alarm_frame.pack(fill = 'both', expand = True)


if __name__ == '__main__':
    App()
