import ttkbootstrap as ttk
from settings import *


class Button(ttk.Button):
	def __init__(self, parent, text, style, func, row, column, span):
		super().__init__(
				master = parent,
				text = text,
				style = style,
				command = func,
				)
		
		self.grid(
				row = row,
				column = column,
				columnspan = span,
				sticky = 'news',
				padx = GAP_SIZE,
				pady = GAP_SIZE
				)
