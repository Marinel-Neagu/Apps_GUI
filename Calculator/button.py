"""
	You need to install the ttkbootstrap, pip install ttkbootstrap(I recomand to use a virtual environment)
"""
import ttkbootstrap as ttk
from settings import GAP_SIZE


class OutputLabel(ttk.Label):
	"""
	Label for result and formula
	"""
	
	def __init__(self, parent, style: str, string_var, row: int, anchor: str, column: int = 0):
		super().__init__(
				master = parent,
				style = style,
				textvariable = string_var,
				)
		self.grid(
				row = row,
				column = column,
				columnspan = 4,
				sticky = anchor
				)


class Button(ttk.Button):
	"""
The class for operators and numbers buttons
	"""
	
	def __init__(self, parent, text: str, func, row: int, column: int, span: int, style: str):
		super().__init__(
				master = parent,
				text = text,
				style = style,
				command = func
				)
		try:
			self.grid(
					row = row,
					column = column,
					columnspan = span,
					sticky = 'news',
					padx = GAP_SIZE,  # is a problem on debian with padx and pady. I am not sure if is on my machine
					# or not.
					pady = GAP_SIZE
					
					)
		except Exception:
			self.grid(
					row = row,
					column = column,
					columnspan = span,
					sticky = 'news',
					
					)


class NumberButtons(Button):
	def __init__(self, parent, text: str, style: str, func: str, row: int, column: int, span: int) -> object:
		super().__init__(
				parent = parent,
				text = text,
				style = style,
				func = lambda: func(text),
				span = span,
				row = row,
				column = column
				)
