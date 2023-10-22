import ttkbootstrap as ttk

from button import Button, OutputLabel, NumberButtons
from settings import (
	APP_SIZE, FONT, NORMAL_FONT_SIZE, OUTPUT_FONT_SIZE,
	MAIN_ROW, MAIN_COLUMN,
	NUMBER_POSITIONS, MATH_POSITIONS, MATH_OPERATORS
	)

try:
	from ctypes import windll, byref, sizeof, c_int
except:
	pass


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'superhero')
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
		
		# set data
		self.formula_string = ttk.StringVar(value = '')
		self.result_string = ttk.StringVar(value = '0')
		self.display_nums = []
		self.full_operation = []
		
		# style
		
		self.Style = ttk.Style()
		self.Style.configure(
				'Result.TLabel',
				font = (FONT, OUTPUT_FONT_SIZE),
				borderwidth = 0,
				)
		
		self.Style.configure(
				'Formula.TLabel',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				)
		
		self.Style.configure(
				'Number.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#4c9be8'
				)
		
		self.Style.configure(
				'Operator.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#4E5D6C',
				)
		self.Style.configure(
				'Operator2.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#4E5D6C',
				)
		
		self.Style.configure(
				'Symbol.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				borderwidth = 0,
				background = '#F0AD4E',
				)
		
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
			TITLE_BAR_COLOR = 0x004C3720
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(TITLE_BAR_COLOR)), sizeof(c_int))
		except:
			pass
	
	def create_labels(self):
		OutputLabel(
				parent = self,
				row = 0,
				anchor = 'SE',
				style = 'Formula.TLabel',
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
			NumberButtons(
					parent = self,
					text = number,
					style = 'Number.TButton',
					func = self.num_press,
					row = data['row'],
					column = data['column'],
					span = data['span'],
					)
	
	def math_symbols(self):
		for data, symbol in MATH_POSITIONS.items():
			self.symbol_button = NumberButtons(
					parent = self,
					text = symbol['text'],
					style = 'Symbol.TButton',
					row = symbol['row'],
					column = symbol['column'],
					span = symbol['span'],
					func = self.math_press
					)
	
	def math_operators(self):
		Button(
				parent = self,
				text = MATH_OPERATORS['clear']['text'],
				style = 'Operator.TButton',
				func = self.clear,
				row = MATH_OPERATORS['clear']['row'],
				column = MATH_OPERATORS['clear']['column'],
				span = MATH_OPERATORS['clear']['span'],
				
				)
		Button(
				parent = self,
				text = MATH_OPERATORS['invert']['text'],
				style = 'Operator.TButton',
				func = self.invert,
				row = MATH_OPERATORS['invert']['row'],
				column = MATH_OPERATORS['invert']['column'],
				span = MATH_OPERATORS['invert']['span'],
				)
		
		Button(
				parent = self,
				text = MATH_OPERATORS['percent']['text'],
				style = 'Operator.TButton',
				func = self.percent,
				row = MATH_OPERATORS['percent']['row'],
				column = MATH_OPERATORS['percent']['column'],
				span = MATH_OPERATORS['percent']['span'],
				)
	
	# 	math logic
	def num_press(self, number):
		self.display_nums.append(number)
		full_number = ''.join(self.display_nums)
		self.result_string.set(full_number)
	
	def invert(self):
		current_number = ''.join(self.display_nums)
		if current_number:
			if float(current_number) > 0:
				self.display_nums.insert(0, '-')
			else:
				del self.display_nums[0]
			self.result_string.set(''.join(self.display_nums))
	
	def percent(self):
		current_number = ''.join(self.display_nums)
		if current_number != '':
			percentage = float(current_number) / 100
			self.display_nums = list(str(percentage))
			self.result_string.set(''.join(self.display_nums))
	
	def clear(self):
		
		self.result_string.set('0')
		
		self.formula_string.set('')
		self.display_nums.clear()
		self.full_operation.clear()
	
	def math_press(self, symbol):
		current_number = ''.join(self.display_nums)
		try:
			if current_number:
				self.full_operation.append(current_number)
				if symbol != '=':
					self.full_operation.append(symbol)
					self.display_nums.clear()
					self.result_string.set('')
					self.formula_string.set(''.join(self.full_operation))
				else:
					formula = ' '.join(self.full_operation)
					result = eval(formula)
					if isinstance(result, float):
						if result.is_integer():
							result = int(result)
						else:
							result = round(result, 5)
					
					self.full_operation.clear()
					self.display_nums = list(str(result))
					
					self.result_string.set(result)
					self.formula_string.set(formula)
		
		except ZeroDivisionError:
			self.result_string.set('Invalid!')
			self.display_nums.clear()
			
			self.formula_string.set('')
			self.full_operation.clear()


CalculatorApp()
