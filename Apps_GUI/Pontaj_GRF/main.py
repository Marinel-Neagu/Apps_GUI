from tkinter import messagebox
from tkinter import colorchooser
import tkinter as tk
from GRF_People import GRF_dictionary
import time


def time_module():
	pass


def version():
	messagebox.showinfo(title='Version', message='Version: 0.1')


def don_t_click():
	if not messagebox.askyesno(title="Don't click ", message='Why did you clicked it? Are you sorry for it?'):
		if not messagebox.askyesno(title='You stuck', message='Are you sorry for it?'):
			while True:
				messagebox.showwarning(title='You are stuck', message='Bro now you are stuck, stop click on it')
		else:
			messagebox.showinfo(title='Goodbye', message='Good, now you should learned your lesson young boy')
	else:
		messagebox.showinfo(title='Goodbye', message='Good,please don t do that again!')


def botton_color():
	color = colorchooser.askcolor()[1]
	buttons_frame.config(bg=str(color))


def font_color():
	global text_label
	color = colorchooser.askcolor()[1]
	text_label.config(fg=str(color))


def center_window(window, height, width):
	screen_width = window.winfo_screenwidth()
	screen_height = window.winfo_screenheight()
	
	x = (screen_width // 2) - (width // 2)
	y = (screen_height // 2) - (height // 2)
	
	window.geometry(f'{width}x{height}+{x}+{y}')


def button(num):
	global text_
	text_ = text_ + str(num)
	text.set(text_)


def delete():
	global text_
	text_ = ''
	text.set(text_)


def enter():
	global text_, numbers_added, text
	try:
		if text_ == '':
			text.set('')
		else:
			id_ = int(text_)
			if id_ not in numbers_added:
				if id_ in GRF_dictionary.values() and id_ != 0:
					for key, value in GRF_dictionary.items():
						if id_ == GRF_dictionary[key]:
							numbers_added.append(id_)
							count = len(numbers_added)
							with open('Pontaj_log.txt', 'a') as Pontaj:
								Pontaj.write(f'{count}. {key}: {time.strftime("%A, %H:%M , %d.%m.%Y")} \n')
								
								text_ = ''
								text.set(f'Buna, {key}!')
				else:
					text.set('Scuze, aceasta persoana \nnu se afla aici 😥!!')
					text_ = ''
			
			
			else:
				
				for k, v in GRF_dictionary.items():
					if id_ == v:
						name_full = k
						name_first = name_full.split(' ')
						text.set(f'Hei,{name_first[0]},deja te ai pontat! ')
						text_ = ''
	except ValueError:
		text.set('')
	except Exception:
		text.set('Sorry this is a bad error!!')


numbers_added = list()
FONT_SIZE = 30
window = tk.Tk()

center_window(window, 600, 600)
window.minsize(600, 600)
window.maxsize(600, 600)
picture_title = tk.PhotoImage(file='Pictures\\contact.png')
window.title('PONTAJ-GRF')
window.iconphoto(False, picture_title)

menubar = tk.Menu(window)
window.config(menu=menubar)

fileMenu = tk.Menu(menubar, tearoff=0, font=('Arial', 15))
menubar.add_cascade(label='Menu', menu=fileMenu)
fileMenu.add_command(label='Exit', command=lambda: quit())

viewMenu = tk.Menu(menubar, tearoff=0, font=('Arial', 15))
menubar.add_cascade(label='Preferance', menu=viewMenu)
viewMenu.add_command(label='Button Color ', command=botton_color)
viewMenu.add_command(label='Font Color', command=font_color)

aboutMenu = tk.Menu(menubar, tearoff=0, font=('Arial', 15))
menubar.add_cascade(label='About', menu=aboutMenu)
aboutMenu.add_command(label='Version ', command=version)
aboutMenu.add_command(label='Don t click', command=don_t_click)

buttons_frame = tk.Frame(window)
buttons_frame.pack(side='bottom')
buttons_frame.pack_configure(fill='both', expand=True)

text_ = ' '
text = tk.StringVar()

text_label = tk.Label(window, font=('Arial', FONT_SIZE), bg='white', width=21, height=3, textvariable=text,
                      wraplength=800)
text_label.pack(side='bottom')
text_label.pack_configure(fill='both', expand=True)

buttons_frame.grid_rowconfigure(0, weight=1)
buttons_frame.grid_rowconfigure(1, weight=1)
buttons_frame.grid_rowconfigure(2, weight=1)
buttons_frame.grid_columnconfigure(0, weight=1)
buttons_frame.grid_columnconfigure(1, weight=1)
buttons_frame.grid_columnconfigure(2, weight=1)
buttons_frame.grid_columnconfigure(3, weight=1)

tk.Button(buttons_frame, text=1, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(1)).grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=2, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(2)).grid(row=0,
                                                                                                               column=1,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=3, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(3)).grid(row=0,
                                                                                                               column=2,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=4, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(4)).grid(row=1,
                                                                                                               column=0,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=5, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(5)).grid(row=1,
                                                                                                               column=1,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=6, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(6)).grid(row=1,
                                                                                                               column=2,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=7, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(7)).grid(row=2,
                                                                                                               column=0,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=8, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(8),
          ).grid(row=2,
                 column=1,
                 sticky='NSEW')
tk.Button(buttons_frame, text=9, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(9)).grid(row=2,
                                                                                                               column=2,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text=0, font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: button(0)).grid(row=2,
                                                                                                               column=3,
                                                                                                               sticky='NSEW')
tk.Button(buttons_frame, text='Delete', font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: delete(

)).grid(
	row=1,
	column=3,
	sticky='NSEW')

tk.Button(buttons_frame, text='Enter', font=('Arial', FONT_SIZE), width=5, height=3, command=lambda: enter()).grid(
	row=0,
	column=3,
	
	sticky='NSEW')

window.mainloop()
