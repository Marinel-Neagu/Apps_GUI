import ttkbootstrap as ttk
from settings import GAP_SIZE


class OutputLabel(ttk.Label):
	def __init__(self, parent, style, string_var, row, anchor):
		super().__init__(
				master = parent,
				style = style,
				textvariable = string_var,
				)
		self.grid(
				column = 0,
				row = row,
				columnspan = 4,
				sticky = anchor
				)


class Button(ttk.Button):
	def __init__(self, parent, text, func, row, column, span):
		super().__init__(
				master = parent,
				text = text,
				command = func
				)
		self.grid(
				row = row,
				column = column,
				columnspan = span,
				sticky = 'news',
				padx = GAP_SIZE,  # is a problem on debian with padx and pady
				pady = GAP_SIZE
				
				)


class NumberButtons(Button):
	def __init__(self, parent, text, func, row, column, span):
		super().__init__(
				parent = parent,
				text = text,
				func = lambda: func(text),
				span = span,
				row = row,
				column = column
				)
