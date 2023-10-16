import ttkbootstrap as ttk


class CalculatorApp(ttk.Window):
	def __init__(self):
		super().__init__(themename = 'cyborg')
		self.mainloop()


CalculatorApp()
