import ttkbootstrap as ttk
import sys, os
from configuration import *
from widgets import BoardGame, BoardScore

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
				style = 'Board.TButton',
				font = (BOARD_GAME_FONT, BOARD_GAME_FONT_SIZE),
				background = '#1F1F1F',
				bordercolor = '#121212',
				borderthickness = 10,
				borderwidth = 2,
				justify = 'center',
				relief = 'solid',
				)
		self.Style.map(
				'Board.TButton',
				foreground = [
						('active', 'white'),
						('disabled', 'white')
						],
				background = [
						('active', '#222222'),
						('disabled', '#222222')]
				)
		self.Style.configure(
				style = 'Reset.TButton',
				font = (RESET_BUTTON_FONT, RESET_BUTTON_FONT_SIZE),
				background = '#e74c3c',
				bordercolor = '#222222',
				borderthickness = 10,
				borderwidth = 2,
				justify = 'center',
				relief = 'solid',
				)
		self.Style.map(
				'Reset.TButton',
				foreground = [
						('active', ''),
						('disabled', 'white')
						],
				background = [
						('active', '#e74c3c'),
						('disabled', '#e74c3c')]
				)
		
		self.Style.configure(
				style = 'Board.TLabel',
				font = (BOARD_SCORE_FONT, BOARD_SCORE_FONT_SIZE),
				foreground = '#E1D9D1'
				
				)
		# 	set player data
		self.player_1 = ttk.IntVar(value = 0)
		self.tie_score = ttk.IntVar(value = 0)
		self.player_2 = ttk.IntVar(value = 0)
		BoardGame(
				parent = self,
				style = 'Board.TButton',
				player_1 = self.player_1,
				tie = self.tie_score,
				player_2 = self.player_2,
				)
		BoardScore(
				parent = self,
				style = 'Board.TLabel',
				style_button = 'Reset.TButton',
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
