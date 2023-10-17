import ttkbootstrap as ttk
from settings import *
from button import Button


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'cyborg')
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
		# set grid layout
		self.rowconfigure(list(range(MAIN_ROW)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMN)), weight = 1, uniform = 'a')
		
		# font and style
		ttk.Style().configure('Result.TLabel', font = (FONT, OUTPUT_FONT_SIZE))
		ttk.Style().configure('Formula.TLabel', font = (FONT, NORMAL_FONT_SIZE))
		ttk.Style().configure(
				'Number.TButton',
				font = (FONT, NORMAL_FONT_SIZE),
				background = '#3e32a8',
				borderwidth = 0,
				)
		
		# set data
		self.formula_string = ttk.StringVar(value = 'Formula')
		self.result_string = ttk.StringVar(value = 'Result')
		
		# set widgets label
		self.formula_label = OutputLabel(
				parent = self,
				row = 0,
				anchor = 'SE',
				style = 'Main.TLabel',
				string_var = self.formula_string
				)
		self.result_label = OutputLabel(
				parent = self,
				row = 1,
				anchor = 'E',
				style = 'Result.TLabel',
				string_var = self.result_string
				
				)
		
		# set widgets buttons and operators
		self.create_widgets()
		
		self.mainloop()
	
	def num_buttons(self):
		for number, data in NUMBER_POSITIONS.items():
			Button(
					parent = self,
					text = number,
					style = 'Number.TButton',
					row = data['row'],
					column = data['column'],
					span = data['span'],
					func = None,
					)
	
	def operator_buttons(self):
		for


class OutputLabel(ttk.Label):
	def __init__(self, parent, style, string_var, row, anchor):
		super().__init__(
				master = parent,
				style = style,
				textvariable = string_var,
				)
		self.grid(column = 0, row = row, columnspan = 4, sticky = anchor)


CalculatorApp()
