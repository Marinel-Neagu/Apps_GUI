import ttkbootstrap as ttk
from configuration import BOARD_SIZE


class BoardGame(ttk.Frame):
	def __init__(self, parent, relx = 0.5, rely = 0.4):
		super().__init__(master = parent)
		self.columnconfigure(list(range(BOARD_SIZE[0])), weight = 1, uniform = 'a')
		self.rowconfigure(list(range(BOARD_SIZE[1])), weight = 1, uniform = 'a')
		
		for i in range(BOARD_SIZE[0]):
			for j in range(BOARD_SIZE[1]):
				Button(
						parent = self,
						row = i,
						column = j,
						text = 'X'
						)
				
				self.pack(expand = True, fill = 'both', anchor = 'center')


class BoardScore(ttk.Frame):
	def __init__(self, parent):
		super().__init__(master = parent)
		self.columnconfigure(0, weight = 1, uniform = 'b')
		self.rowconfigure((0, 1), weight = 1, uniform = 'b')
		Labels(
				parent = self,
				text = 'Score',
				row = 0,
				column = 0
				)
		
		self.pack(expand = True, fill = 'both', anchor = 'center')


class Labels(ttk.Label):
	def __init__(self, parent, text, row, column):
		super().__init__(
				master = parent,
				text = text,
				)
		self.grid(
				row = row,
				column = column,
				sticky = 'news',
				)


class Button(ttk.Button):
	def __init__(self, parent, text, row, column):
		super().__init__(
				master = parent,
				text = text
				)
		self.grid(
				row = row,
				column = column,
				sticky = 'news',
				# expand = True,
				# fill = 'both'
				)
