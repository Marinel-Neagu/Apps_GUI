import time
from PIL import ImageTk, Image

Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from widgets import *

try:
	from ctypes import windll, byref, sizeof, c_int
except Exception:
	pass


class App(ttk.Window):
	def __init__(self) -> None:
		super().__init__(themename = 'solar')
		self.bind('<Alt-s>', lambda _: self.destroy())
		self.title(TITLE)
		
		# set image title bar
		try:
			image_path = "..\Front_end\Images\clock.ico"
			self.iconbitmap(image_path)
		except:
			pass
		
		# set color title bar
		try:
			HWND = windll.user32.GetParent(self.winfo_id())
			windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(COLOR_TITLE_BAR)), sizeof(c_int))
		except NameError:
			pass
		
		# geometry window
		left = int(self.winfo_screenwidth() / 2 - WIDTH_MAIN / 2)
		top = int(self.winfo_screenheight() / 2 - HEIGHT_MAIN / 2)
		self.geometry(f'{WIDTH_MAIN}x{HEIGHT_MAIN}+{left}+{top}')
		
		# set title bar color
		try:
			self.update()
			HWND = windll.user32.GetParent(self.winfo_id())
			title_bar_color = 0x00000000
			windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))
		except Exception:
			pass
		
		#  put the layout
		self.layout = MainLayout(self)
		self.layout.pack(expand = True, fill = 'both')
		
		# run
		self.mainloop()


class MainLayout(ttk.Notebook):
	"""
Main Layout for the clock, all the 4 layout are put together
	"""
	
	def __init__(self, parent):
		super().__init__(master = parent)
		# set tabs
		self.clock_layout = ClockTab(self)
		self.timer_layout = TimerTab(self)
		self.alarm_layout = AlarmTab(self)
		self.stopwatch_layout = StopWatchTab(self)
		
		# add tabs
		self.add(self.timer_layout, text = 'Timer')
		self.add(self.clock_layout, text = 'Clock')
		self.add(self.alarm_layout, text = 'Alarm')
		self.add(self.stopwatch_layout, text = 'StopWatch')


class ClockTab(ttk.Frame):
	"""
Layout for the clock
	"""
	
	def __init__(self, parent):
		super().__init__(master = parent)
		
		# clock widgets
		self.frame_clock = FrameClock(self)
		self.frame_clock.pack(expand = True, fill = "both")
		
		self.frame_water = FrameWeather(self)
		self.frame_water.pack(expand = True, fill = "both")


class TimerTab(ttk.Frame):
	"""
Layout for the timer
	"""
	
	def __init__(self, parent):
		super().__init__(master = parent)
		self.button = ttk.Button(self, text = 'Play', command = self.play)
		
		self.button.pack()
	
	def play(self) -> None:
		pass


class AlarmTab(ttk.Frame):
	"""
Add the alarma layout
	"""
	
	def __init__(self, parent: str) -> None:
		super().__init__(master = parent)
		self.button = ttk.Button(self)


# widgets clock


class StopWatchTab(ttk.Frame):
	"""
Layout for the StopWatch
	"""
	
	def __init__(self, parent):
		super().__init__(master = parent)
		clock_time = ttk.Label(self, text = 'Stop Watch ')
		clock_time.pack()
		self.pack(expand = True, fill = 'both')
		self.pack()


if __name__ == '__main__':
	App()
