import ttkbootstrap as ttk
import sys, os
from configuration import MAIN_SIZE, BOARD_FONT_SIZE, BOARD_FONT, SCORE_FONT_SIZE, SCORE_FONT
from widgets import BoardGame, BoardScore

# add the color title.(it works only on windows)
try:
	from ctypes import windll, byref, sizeof, c_int
except Exception:
	pass


class Application(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'superhero')
		self.bind('<Alt-s>', lambda event: self.destroy())
		self.title('')
		self.set_emtpy_icon()
		self.set_window_size(width = MAIN_SIZE[0], height = MAIN_SIZE[1])
		
		# set up the style
		self.Style = ttk.Style()
		self.Style.configure(
				style = 'Board.TButton',
				font = (BOARD_FONT, BOARD_FONT_SIZE),
				background = '#2B4155',
				bordercolor = '#FFF',
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
						('active', '#2B4155'),
						('disabled', '#2B4155')]
				)
		
		self.Style.configure(
				style = 'Board.TLabel',
				font = (SCORE_FONT, SCORE_FONT_SIZE),
				
				)
		
		BoardGame(parent = self, style = 'Board.TButton')
		BoardScore(parent = self, style = 'Board.TLabel')
		
		# set layout
		
		self.mainloop()
	
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
