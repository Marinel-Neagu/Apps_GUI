import ttkbootstrap as ttk


class AlarmsFrame(ttk.Frame):
    def __init__(self, parent, text):
        self.style = ttk.Style()
        self.style.configure('Frame.TFrame', background = 'red')
        super().__init__(master = parent, style = 'Frame.TFrame')
        
        # set grid layout
        self.rowconfigure((0, 1), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(0, 7)), weight = 1, uniform = 'a')
        
        #  set data
        self.time_str = text
        self.variable_checkbutton = ttk.IntVar()
        
        # set widgets
        self.time_label = ttk.Label(
                master = self,
                text = self.time_str,
                background = 'red',
                
                )
        
        self.checkbutton = ttk.Checkbutton(
                master = self,
                variable = self.variable_checkbutton,
                onvalue = 0,
                offvalue = 1,
                command = lambda: print('something')
                )
        # set layout
        self.time_label.grid(row = 0, column = 0, sticky = 'news')
        self.checkbutton.grid(row = 0, column = 6, sticky = 'news ')
        # add the layer of day
        self.add_days()
    
    def add_days(self):
        list_day = ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
        for index, day in enumerate(list_day):
            DayButton(
                    parent = self,
                    day_name = day,
                    row = 1,
                    column = index
                    )


class DayButton(ttk.Button):
    def __init__(self, parent, day_name, row, column, ):
        super().__init__(
                master = parent,
                text = day_name,
                command = lambda: print(day_name)
                )
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                padx = 2,
                pady = 2
                
                )
