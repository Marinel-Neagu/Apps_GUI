import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.bind('<Alt-s>', lambda even: self.destroy())
        self.geometry('400X400')
        self.title('')
        self.set_icon('images/empty.ico')
        
        self.mainloop()
    
    def set_icon(self, path):
        try:
            self.iconbitmap(path)
        except Exception:
            pass


if __name__ == '__main__':
    App()
