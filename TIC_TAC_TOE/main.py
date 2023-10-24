import ttkbootstrap as ttk
import random


class Application(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'superhero')
		self.title('TIC TAC TOE')
		self.iconbitmap('')
		self.geometry('400x400')
		self.mainloop()


class Labels(ttk.Button):
	pass


class Button(ttk.Button):
	pass


if __name__ == '__main__':
	Application()
