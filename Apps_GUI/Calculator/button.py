import ttkbootstrap as ttk
from settings import *


class Button(ttk.Button):
	def __init__(self, parent, text, style, row, col, span):
		super().__init__(
				master = parent,
				text = text,
				style = style,
				
				)
		self.grid(row = row, column = col, rowspan = span, padx = GAP_SIZE, pady = GAP_SIZE)
