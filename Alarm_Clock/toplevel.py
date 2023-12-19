import ttkbootstrap as ttk
import tkinter as tk


class TopLevel(tk.Toplevel):
    def __init__(self, parent, hour_int, minute_int, ok_function, cancel_function):
        super().__init__(master = parent)
        
        # set attributes
        
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('Clock')
        self.set_geometry(width = 300, height = 300)
        self.attributes('-type', 'dock')
        
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
