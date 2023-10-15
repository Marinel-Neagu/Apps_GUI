import tkinter as tk
import customtkinter as ctk
from Settings import *


class CalculatorApp(ctk.CTk):
	def __init__(self):
		super().__init__()
		# set window
		
		ctk.set_default_color_theme('blue')
		self.bind('<Alt-s>', lambda event: self.destroy())
		self.title('Calculator App')
		top = int((self.winfo_screenheight() / 2) - (HEIGHT / 2))
		left = int((self.winfo_screenwidth() / 2) - (WIDTH / 2))
		
		self.geometry(f'{HEIGHT}x{WIDTH}+{left}+{top}')
		
		# set data
		
		# set widgets
		self.entries = CalculatorEntry(self)
		self.buttons = CalculatorButton(self)
		
		# set layout
		self.entries.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.38)
		self.buttons.place(relx = 0.015, rely = 0.38)
		
		self.mainloop()


class CalculatorEntry(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(master = parent)
		
		# set row and columns
		
		self.row_data = list(range(5))
		self.col_data = list(range(4))
		
		# set layout
		
		self.columnconfigure(self.col_data, weight = 1, uniform = 'a')
		self.rowconfigure(self.row_data, weight = 1, uniform = 'a')
		
		# set variables
		
		self.entry = tk.StringVar(value = '')
		self.formula_entry = tk.StringVar(value = '')
		
		# set widgets for entry
		
		label_calculator = ctk.CTkLabel(
				self,
				textvariable = self.entry,
				fg_color = 'blue',
				
				)
		entry_calculator = ctk.CTkLabel(
				self,
				textvariable = self.formula_entry,
				fg_color = 'red',
				
				)
		
		# layout widgets
		label_calculator.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.3)
		entry_calculator.place(relx = 0, rely = 0.3, relwidth = 1, relheight = 0.7)


class CalculatorButton(ctk.CTkFrame):
	def __init__(self, parent):
		super().__init__(master = parent)
		
		self.button(text_button = '%', row_button = 0, col_button = 0)
		self.button(text_button = 'C', row_button = 0, col_button = 1)
		self.button(text_button = 'B', row_button = 0, col_button = 2)
		self.button(text_button = ':', row_button = 0, col_button = 3)
		
		self.button(text_button = '7', row_button = 1, col_button = 0)
		self.button(text_button = '8', row_button = 1, col_button = 1)
		self.button(text_button = '9', row_button = 1, col_button = 2)
		self.button(text_button = 'X', row_button = 1, col_button = 3)
		
		self.button(text_button = '4', row_button = 2, col_button = 0)
		self.button(text_button = '5', row_button = 2, col_button = 1)
		self.button(text_button = '6', row_button = 2, col_button = 2)
		self.button(text_button = '-', row_button = 2, col_button = 3)
		
		self.button(text_button = '1', row_button = 3, col_button = 0)
		self.button(text_button = '2', row_button = 3, col_button = 1)
		self.button(text_button = '3', row_button = 3, col_button = 2)
		self.button(text_button = '+', row_button = 3, col_button = 3)
		
		self.button(text_button = '-/+', row_button = 4, col_button = 0)
		self.button(text_button = '0', row_button = 4, col_button = 1)
		self.button(text_button = '.', row_button = 4, col_button = 2)
		self.button(text_button = '=', row_button = 4, col_button = 3)
	
	def button(self, text_button, row_button, col_button, ):
		button_calculator = ctk.CTkButton(
				self,
				text = text_button,
				height = 50,
				width = 90,
				font = ("Arial", 20),
				command = self.function_button(text_button),
				)
		button_calculator.grid(
				
				row = row_button,
				column = col_button,
				pady = 1, sticky = 'news',
				padx = 1
				
				)
	
	def function_button(self, num):
		CalculatorEntry(self).entry.set(num)


CalculatorApp()
