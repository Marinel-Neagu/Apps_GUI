import ttkbootstrap as ttk
from settings import *
from button import *

try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__()
		self.bind('<Alt-s>', lambda e: self.destroy())
		# setup
		self.title("")
		self.left = int((self.winfo_screenwidth() - APP_SIZE[0]) / 2)
		self.top = int((self.winfo_screenheight() - APP_SIZE[1]) / 2)
		self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}+{self.left}+{self.top}")
		try:
			self.iconbitmap('image/empty.ico')
		except:
			pass
		# set title bar color (only on windows is working)
		self.set_title_bar_color()
		
		# set grid layout
		self.rowconfigure(list(range(MAIN_ROW)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMN)), weight = 1, uniform = 'a')
		
		# font and style
		ttk.Style().configure('Result.TLabel', font = (FONT, OUTPUT_FONT_SIZE))
		ttk.Style().configure('Formula.TLabel', font = (FONT, NORMAL_FONT_SIZE))
		ttk.Style().configure(
				'TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				background = '#3e32a8',
				borderwidth = 0,
				)
		
		# set data
		self.formula_string = ttk.StringVar(value = '')
		self.result_string = ttk.StringVar(value = '0')
		self.display_nums = []
		self.full_operation = []
		
		# set widgets label
		self.create_labels()
		
		# set widgets buttons and operators
		self.num_buttons()
		self.math_symbols()
		self.math_operators()
		
		self.mainloop()
	
	def set_title_bar_color(self):
		
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			DWMWA_ATTRIBUTE = 35
			TITLE_BAR_COLOR = 0x00000000
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(TITLE_BAR_COLOR)), sizeof(c_int))
		
		except:
			print('This is not working on macOS and GNU/Linux.:/')
	
	def create_labels(self):
		OutputLabel(
				parent = self,
				row = 0,
				anchor = 'SE',
				style = 'Main.TLabel',
				string_var = self.formula_string
				)
		OutputLabel(
				parent = self,
				row = 1,
				anchor = 'E',
				style = 'Result.TLabel',
				string_var = self.result_string
				
				)
	
	def num_buttons(self):
		for number, data in NUMBER_POSITIONS.items():
			Button(
					parent = self,
					text = number,
					func = self.num_press,
					row = data['row'],
					column = data['column'],
					span = data['span'],
					)
	
	def math_symbols(self):
		for data, symbol in MATH_POSITIONS.items():
			Button(
					parent = self,
					text = symbol['text'],
					row = symbol['row'],
					column = symbol['column'],
					span = symbol['span'],
					func = None
					)
	
	def math_operators(self):
		for data, operator in MATH_OPERATORS.items():
			Button(
					parent = self,
					text = operator['text'],
					func =None ,
					row = operator['row'],
					column = operator['column'],
					span = operator['span'],
					)
	
	# 	math logic
	def num_press(self, number):
		self.display_nums.append(number)
		full_operation = ''.join(self.display_nums)
		self.result_string.set(full_operation)
	
	def clear(self):
		self.result_string.set('0')
		self.formula_string.set('')
		self.display_nums.clear()
		self.full_operation.clear()


CalculatorApp()
