import ttkbootstrap as ttk
from time import sleep
from configuration import BOARD_SIZE


# set the Board with X and 0
class BoardGame(ttk.Frame):
	def __init__(self, parent, style):
		super().__init__(master = parent)
		# set data
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
						)
	
	def next_turn(self, row, column):
		# Check if the button is empty and no winner has been determined yet
		if self.board_position[row][column]['text'] == "" and self.check_winner() is False:
			
			if self.player == self.players_list[0]:
				# Set the button text to the current player's symbol
				self.board_position[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					# Switch to the next player's turn
					self.player = self.players_list[1]
			else:
				self.board_position[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					self.player = self.players_list[0]
		else:
			self.new_game()
	
	def check_winner(self):
		for row in range(3):
			if self.board_position[row][0]['text'] == self.board_position[row][1]['text'] == \
					self.board_position[row][2]['text'] != '':
				return True
		for column in range(3):
			if self.board_position[0][column]['text'] == self.board_position[1][column]['text'] == \
					self.board_position[2][column]['text'] != '':
				return True
		if self.board_position[0][0]['text'] == self.board_position[1][1]['text'] == \
				self.board_position[2][2]['text'] != '':
			return True
		elif self.board_position[0][2]['text'] == self.board_position[1][1]['text'] == \
				self.board_position[2][0]['text'] != '':
			return True
		elif self.empty_space() is False:
			print('is not empty')
		else:
			return False
	
	def empty_space(self):
		empty_space = 9
		for row in range(3):
			for col in range(3):
				if self.board_position[row][col]['text'] != '':
					empty_space -= 1
		if empty_space == 0:
			return False
		else:
			return True
	
	def new_game(self):
		sleep(2)
		for row in range(3):
			for col in range(3):
				self.board_position[row][col]['text'] = ''


# set the Board Score Frame, it contains the bottom labels


class BoardScore(ttk.Frame):
	def __init__(self, parent, style):
		super().__init__(master = parent)
		# data score
		self.player_1_score = ttk.IntVar(value = 0)
		self.player_2_score = ttk.IntVar(value = 0)
		self.tie_score = ttk.IntVar(value = 0)
		
		self.columnconfigure(list(range(5)), weight = 1, uniform = 'b')
		self.rowconfigure((0, 1), weight = 1, uniform = 'b')
		self.pack(fill = 'both', side = 'bottom')
		
		# show players name
		self.player_1 = Labels(
				parent = self,
				textvariable = None,
				text = 'Player 1(x)',
				row = 0,
				column = 0,
				columnspan = 2,
				style = style,
				)
		self.tie = Labels(
				parent = self,
				textvariable = None,
				text = 'Tie ',
				row = 0,
				column = 2,
				columnspan = 2,
				style = style,
				)
		
		self.player_2 = Labels(
				parent = self,
				textvariable = None,
				text = 'Player 2(o)',
				row = 0,
				column = 4,
				columnspan = 2,
				style = style,
				)
		# show score
		self.label_player_1_score = Labels(
				parent = self,
				textvariable = self.player_1_score,
				text = '',
				row = 1,
				column = 0,
				columnspan = 2,
				style = style,
				
				)
		
		self.label_tie_score = Labels(
				parent = self,
				textvariable = self.tie_score,
				text = '',
				row = 1,
				column = 2,
				columnspan = 2,
				style = style,
				)
		self.label_player_2_score = Labels(
				parent = self,
				textvariable = self.player_2_score,
				text = '',
				row = 1,
				column = 4,
				columnspan = 2,
				
				style = style,
				)


class Button(ttk.Button):
	
	def __init__(self, parent, text, command, row, column, style):
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
