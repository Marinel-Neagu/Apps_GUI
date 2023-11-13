import ttkbootstrap as ttk
from configuration import BOARD_SIZE


class BoardGame(ttk.Frame):
	def __init__(self, parent, style, player_1, tie, player_2, ):
		super().__init__(master = parent)
		# set data
		self.player_1 = player_1
		self.tie_score = tie
		self.player_2 = player_2
		self.x_score = 0
		self.o_score = 0
		self.t_score = 0
		self.players_list = ['X', 'O']
		self.player = self.players_list[0]
		self.board_position = [
				[0, 0, 0],
				[0, 0, 0],
				[0, 0, 0]
				]
		# layout
		
		self.columnconfigure(list(range(BOARD_SIZE[0])), weight = 1, uniform = 'a')
		self.rowconfigure(list(range(BOARD_SIZE[1])), weight = 1, uniform = 'a')
		self.pack(expand = True, fill = 'both', side = 'top')
		# widgets
		
		for rows in range(BOARD_SIZE[0]):
			for cols in range(BOARD_SIZE[1]):
				self.board_position[rows][cols] = Button(
						parent = self,
						text = '',
						command = lambda row = rows, column = cols: self.next_turn(row, column),
						row = rows,
						column = cols,
						style = style,
						columnspan = 1,
						rowspan = 1,
						)
	
	def next_turn(self, row, column):
		
		if self.board_position[row][column]['text'] == "" and self.check_winner() is False:
			
			if self.player == self.players_list[0]:
				
				self.board_position[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					self.player = self.players_list[1]
				
				elif self.check_winner() is True:
					self.player_1.set(self.player_1.get() + 1)
				
				elif self.check_winner() == "Tie":
					self.tie_score.set(self.tie_score.get() + 1)
			
			else:
				self.board_position[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					self.player = self.players_list[0]
				elif self.check_winner() is True:
					self.player_2.set(self.player_2.get() + 1)
				
				elif self.check_winner() == "Tie":
					self.tie_score.set(self.tie_score.get() + 1)
		else:
			
			if self.empty_spaces() is False or self.check_winner() is True:
				self.clean_board()
	
	def check_winner(self):
		# Check for winning conditions
		for row in range(3):
			if self.board_position[row][0]['text'] == self.board_position[row][1]['text'] == \
					self.board_position[row][2]['text'] != "":
				return True
		
		for column in range(3):
			if self.board_position[0][column]['text'] == self.board_position[1][column]['text'] == \
					self.board_position[2][column]['text'] != "":
				return True
		
		if self.board_position[0][0]['text'] == self.board_position[1][1]['text'] == \
				self.board_position[2][2]['text'] != "":
			return True
		
		elif self.board_position[0][2]['text'] == self.board_position[1][1]['text'] == \
				self.board_position[2][0]['text'] != "":
			return True
		elif self.empty_spaces() is False:
			return 'Tie'
		else:
			return False
	
	def empty_spaces(self):
		spaces = 9
		for row in range(3):
			for column in range(3):
				if self.board_position[row][column]['text'] != '':
					spaces -= 1
		if spaces == 0:
			return False
		else:
			return True
	
	def clean_board(self):
		# Clear the button texts and backgrounds
		for row in range(3):
			for column in range(3):
				self.board_position[row][column]['text'] = ''


class BoardScore(ttk.Frame):
	
	def __init__(
			self,
			parent,
			style,
			player_1,
			tie,
			player_2,
			function,
			style_button,
			):
		super().__init__(master = parent)
		# data score
		self.player_1_score = player_1
		self.player_2_score = player_2
		self.tie_score = tie
		
		self.columnconfigure(list(range(10)), weight = 1, uniform = 'b')
		self.rowconfigure((0, 1), weight = 1, uniform = 'b')
		self.pack(fill = 'both', side = 'bottom')
		
		# show players name
		self.player_1 = Labels(
				parent = self,
				textvariable = None,
				text = 'Player 1(x)',
				row = 0,
				column = 0,
				columnspan = 3,
				style = style,
				)
		self.tie = Labels(
				parent = self,
				textvariable = None,
				text = 'Tie ',
				row = 0,
				column = 4,
				columnspan = 2,
				style = style,
				)
		
		self.player_2 = Labels(
				parent = self,
				textvariable = None,
				text = 'Player 2(o)',
				row = 0,
				column = 6,
				columnspan = 3,
				style = style,
				)
		self.reset_button = Button(
				parent = self,
				text = 'Reset\nGame',
				command = function,
				row = 0,
				column = 9,
				columnspan = 3,
				rowspan = 2,
				style = style_button,
				
				)
		# show score
		self.label_player_1_score = Labels(
				parent = self,
				textvariable = self.player_1_score,
				text = '',
				row = 1,
				column = 0,
				columnspan = 3,
				style = style,
				
				)
		
		self.label_tie_score = Labels(
				parent = self,
				textvariable = self.tie_score,
				text = '',
				row = 1,
				column = 4,
				columnspan = 2,
				style = style,
				)
		self.label_player_2_score = Labels(
				parent = self,
				textvariable = self.player_2_score,
				text = '',
				row = 1,
				column = 6,
				columnspan = 3,
				style = style,
				)


class Button(ttk.Button):
	
	def __init__(self, parent, text, command, row, column, columnspan, rowspan, style):
		# set data
		super().__init__(
				master = parent,
				text = text,
				command = command,
				style = style,
				)
		
		# set layout
		self.grid(
				row = row,
				column = column,
				sticky = 'news',
				columnspan = columnspan,
				rowspan = rowspan,
				)


class Labels(ttk.Label):
	def __init__(self, parent, text, textvariable, row, column, columnspan, style):
		super().__init__(
				master = parent,
				text = text,
				textvariable = textvariable,
				style = style,
				anchor = 'center',
				)
		
		self.grid(
				row = row,
				column = column,
				sticky = 'news',
				padx = 10,
				pady = 10,
				columnspan = columnspan
				)
