import ttkbootstrap as ttk
import random, sys, os
from configuration import MAIN_SIZE
from widgets import BoardGame, BoardScore


class Application(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'superhero')
		self.bind('<Alt-s>', lambda event: self.destroy())
		self.title('TIC TAC TOE')
		self.set_emtpy_icon()
		self.set_window_size(MAIN_SIZE[0], MAIN_SIZE[1])
		
		# set layout
		self.board_game = BoardGame(self, relx = 0, rely = 0)
		self.board_score = BoardScore(self)
		
		self.mainloop()
	
	def set_emtpy_icon(self):
		try:
			path_image = self.path_resource('empty.ico')
			self.iconbitmap(path_image)
		except Exception:
			pass
	
	def path_resource(self, relativ_path):
		try:
			base_path = sys._MEIPASS
		except Exception:
			base_path = os.path.abspath('.')
		return os.path.join(base_path, relativ_path)
	
	def set_window_size(self, width, height):
		left = int(self.winfo_screenwidth() / 2 - width / 2)
		top = int(self.winfo_screenheight() / 2 - height / 2)
		self.geometry(f'{width}x{height}+{left}+{top}')
	
	def set_title_bar_color(self):
		pass


if __name__ == '__main__':
	Application()
