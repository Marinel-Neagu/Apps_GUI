import os
from tkinter import *
from tkinter import Menu, messagebox
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def open_file():
    pass


def save_file():
    pass


def save_as_file():
    pass


def new_file():
    pass


def cut():
    text_area.event_generate('<<Cut>>')


def copy():
    text_area.event_generate('<<Copy>>')


def paste():
    text_area.event_generate('<<Paste>>')


def background_color():
    color = colorchooser.askcolor()[1]
    text_area.config(bg=color)


def font_color():
    color = colorchooser.askcolor()[1]
    text_area.config(fg=color)


def font_style():
    pass


def version():
    messagebox.showinfo(title="Version", message="Version:0.1")


window = Tk()
window.title('Journal')

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('Arial', 10))
menubar.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label='Open', command=open_file)

fileMenu.add_command(label='New', command=save_file)

fileMenu.add_command(label='Save', command=new_file)
fileMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menubar, tearoff=0, font=('Arial', 10))
menubar.add_cascade(label='Edit', menu=editMenu)

editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)

viewMenu = Menu(menubar, tearoff=0, font=('Arial', 10))
menubar.add_cascade(label='View', menu=viewMenu)

viewMenu.add_command(label='Background', command=background_color, underline=1)
viewMenu.add_command(label='Font Color', command=font_color)
viewMenu.add_command(label='Font Style', command=font_style)

helpMenu = Menu(menubar, tearoff=0, font=('Arial', 10))
menubar.add_cascade(label='Help', menu=helpMenu)

subMenu = Menu(menubar, tearoff=0, font=('Arial', 10))
subMenu.add_command(label='Info', command=version)
subMenu.add_command(label='Get some help!', command=save_as_file)
helpMenu.add_cascade(label='About', menu=subMenu)

text_area = Text(window, font=('Ink Free', 20), fg='blue')

text_area.pack()


window.mainloop()
