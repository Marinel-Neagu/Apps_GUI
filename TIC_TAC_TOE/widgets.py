import ttkbootstrap as ttk
from configuration import BOARD_SIZE


class BoardGame(ttk.Frame):
	def __init__(self, parent, style, relx, rely, relheight, relwidth):
		super().__init__(master = parent)
		self.columnconfigure(list(range(BOARD_SIZE[0])), weight = 1, uniform = 'a')
		self.rowconfigure(list(range(BOARD_SIZE[1])), weight = 1, uniform = 'a')
		
		for i in range(BOARD_SIZE[0]):
			for j in range(BOARD_SIZE[1]):
				Button(
						parent = self,
						row = i,
						column = j,
						text = '',
						style = style,
						)
		self.place(
				relx = relx,
				rely = rely,
				relwidth = relwidth,
				relheight = relheight
				)


class BoardScore(ttk.Frame):
	def __init__(self, parent, relx, rely, relwidth, relheight):
		super().__init__(master = parent)
		self.columnconfigure(list(range(5)), weight = 1, uniform = 'b')
		self.rowconfigure((0, 1), weight = 1, uniform = 'b')
		self.place(relx = relx, rely = rely)
		self.player_1 = Labels(
				self,
				text = 'Player 1',
				row = 0,
				column = 0
				)
		
		self.player_2 = Labels(
				self,
				text = 'Player 2',
				row = 1,
				column = 0
				)
		self.place(relx = relx, rely = rely, relwidth = relwidth, relheight = relheight)


class Button(ttk.Button):
	def __init__(self, parent, text, row, column, style):
		super().__init__(
				master = parent,
				text = text,
				style = style
				)
		self.grid(
				row = row,
				column = column,
				sticky = 'news',
				padx = 10,
				pady = 10
				)


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
