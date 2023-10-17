import ttkbootstrap as ttk
from settings import *


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'cyborg')
		self.bind('<Alt-s>', lambda e: self.destroy())
		# setup
		self.title("")
		self.left = int((self.winfo_screenwidth() - APP_SIZE[1]) / 2)
		self.top = int((self.winfo_screenheight() - APP_SIZE[0]) / 2)
		self.geometry(f"{APP_SIZE[0]}x{APP_SIZE[1]}+{self.top}+{self.left}")
		try:
			self.iconbitmap('image/empty.ico')
		except:
			pass
		# set grid layout
		self.rowconfigure(list(range(MAIN_ROW)), weight = 1, uniform = 'a')
		self.columnconfigure(list(range(MAIN_COLUMN)), weight = 1, uniform = 'a')
		
		# font and style
		self.main_font = ttk.Style()
		self.main_font.configure('Main.TLabel', font = (FONT, NORMAL_FONT_SIZE))
		self.result_font = ttk.Style()
		self.result_font.configure('Result.TLabel', font = (FONT, OUTPUT_FONT_SIZE))
		
		# set data
		self.formula_string = ttk.StringVar(value = 'Formula')
		self.result_string = ttk.StringVar(value = 'Result')
		
		# set widgets
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
				string_var =
				self.result_string
				)
		
		self.mainloop()
	
	def create_widgets(self):
		pass


class OutputLabel(ttk.Label):
	def __init__(self, parent, style, string_var, row, anchor):
		super().__init__(
				master = parent,
				style = style,
				textvariable = string_var
				
				)
		self.grid(column = 0, row = row, columnspan = 4, sticky = anchor)


CalculatorApp()
