import ttkbootstrap as ttk
import sys, os
from widgets import BoardGame, BoardScore
from configuration import (
	
	# layout
	MAIN_SIZE,
	BOARD_SIZE,
	BOARD_SCORE_SIZE,
	# style
	BOARD_GAME,
	BOARD_SCORE,
	RESET_BUTTON,
	)

# add the color title.(it works only on windows)
try:
	from ctypes import windll, byref, sizeof, c_int
except Exception:
	pass


class Application(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'darkly')
		self.bind('<Alt-s>', lambda event: self.destroy())
		self.title('')
		self.set_emtpy_icon()
		self.set_window_size(width = MAIN_SIZE[0], height = MAIN_SIZE[1])
		
		# set up the style
		self.Style = ttk.Style()
		self.Style.configure(
				style = 'BoardGame.TButton',
				font = (BOARD_GAME['FONT'], BOARD_GAME['FONT_SIZE']),
				background = BOARD_GAME['BACKGROUND'],
				bordercolor = BOARD_GAME['BORDER_COLOR'],
				borderthickness = BOARD_GAME['BORDER_THICKNESS'],
				borderwidth = BOARD_GAME['BORDER_WIDTH'],
				justify = BOARD_GAME['JUSTIFY'],
				relief = BOARD_GAME['RELIEF']
				)
		self.Style.map(
				'BoardGame.TButton',
				foreground = [
						('active', 'red'),
						('disabled', 'red')
						],
				background = [
						('active', BOARD_GAME['HOVER_COLOR_ACTIVE']),
						('disabled', BOARD_GAME['HOVER_COLOR_DISABLED'])
						]
				)
		
		self.Style.configure(
				style = 'ResetButton.TButton',
				font = (RESET_BUTTON['FONT'], RESET_BUTTON['SIZE']),
				background = RESET_BUTTON['BACKGROUND'],
				bordercolor = RESET_BUTTON['BORDER_COLOR'],
				borderthickness = RESET_BUTTON['BORDER_THICKNESS'],
				borderwidth = RESET_BUTTON['BORDER_WIDTH'],
				justify = RESET_BUTTON['JUSTIFY'],
				relief = RESET_BUTTON['RELIEF']
				)
		self.Style.map(
				'ResetButton.TButton',
				foreground = [
						('active', RESET_BUTTON['TEXT_COLOR_ACTIVE']),
						('disabled', RESET_BUTTON['TEXT_COLOR_DISABLED'])
						],
				background = [
						('active', RESET_BUTTON['HOVER_COLOR_ACTIVE']),
						('disabled', RESET_BUTTON['HOVER_COLOR_DISABLED'])]
				)
		
		self.Style.configure(
				style = 'BoardScore.TLabel',
				font = (BOARD_SCORE['FONT'], BOARD_SCORE['FONT_SIZE']),
				foreground = BOARD_SCORE['TEXT_COLOR']
				
				)
		# 	set player data
		self.player_1 = ttk.IntVar(value = 0)
		self.tie_score = ttk.IntVar(value = 0)
		self.player_2 = ttk.IntVar(value = 0)
		BoardGame(
				parent = self,
				style = 'BoardGame.TButton',
				player_1 = self.player_1,
				tie = self.tie_score,
				player_2 = self.player_2,
				)
		BoardScore(
				parent = self,
				style = 'BoardScore.TLabel',
				style_button = 'ResetButton.TButton',
				player_1 = self.player_1,
				tie = self.tie_score,
				player_2 = self.player_2,
				function = self.clean_board
				)
		
		self.mainloop()
	
	def clean_board(self):
		self.player_1.set(0)
		
		self.player_2.set(0)
		self.tie_score.set(0)
	
	def set_emtpy_icon(self):
		try:
			path_image = self.path_resource('empty.ico')
			self.iconbitmap(path_image)
		except Exception:
			pass
	
	def path_resource(self, relative_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath('.')
		return os.path.join(base_path, relative_path)
	
	def set_window_size(self, width, height):
		left = int(self.winfo_screenwidth() / 2 - width / 2)
		top = int(self.winfo_screenheight() / 2 - height / 2)
		self.geometry(f'{width}x{height}+{left}+{top}')
	
	def set_title_bar_color(self):
		"""
	It works only on Windows, not on GNU/Linux and macOS.
		"""
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			DWMWA_ATTRIBUTE = 35
			TITLE_BAR_COLOR = 0x00000000
			windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(TITLE_BAR_COLOR)), sizeof(c_int))
		except Exception:
			pass


if __name__ == '__main__':
	Application()
