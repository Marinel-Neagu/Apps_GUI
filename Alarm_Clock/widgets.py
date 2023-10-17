from PIL import Image

Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from lorem_text import lorem
from settings import *
import time
from time_window import *


class FrameClock(ttk.Frame):
	def __init__(self, parent):
		super().__init__(master = parent)
		
		# layout clock
		style = ttk.Style()
		style.configure('ClockStyle.TLabel', font = ("Arial", 80), background = '#073642')
		style.configure('DataStyle.TLabel', font = ("Arial", 30), background = '#073642')
		
		# add widgets
		
		self.clock_label = ttk.Label(self, style = "ClockStyle.TLabel")
		self.clock_label.configure(anchor = 'center')
		
		self.date_label = ttk.Label(self, style = 'DataStyle.TLabel')
		self.date_label.configure(anchor = 'center')
		
		# set layout
		
		self.clock_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.4, anchor = 'nw')
		
		self.clock = self.update_clock()
		
		self.date_label.place(relx = 0.0, rely = 0.4, relwidth = 1, relheight = 0.2, anchor = 'nw')
		self.update_date()
	
	def update_clock(self):
		time_format = '%H:%M:%S'
		clock_time_digits = time.strftime(time_format)
		
		self.clock_label.configure(text = clock_time_digits)
		self.after(1000, self.update_clock)
	
	def update_date(self):
		time_format = '%a %d.%m.%Y'
		date_format = time.strftime(time_format)
		
		self.date_label.configure(text = date_format)
		self.after(1000, self.update_date)


class FrameWeather(ttk.Frame):
	def __init__(self, parent):
		super().__init__(master = parent)
		self.date_label = ttk.Label(self, text = lorem.sentence(), style = 'TLabel')
		
		self.date_label.pack(expand = True, fill = 'both')


class FrameWidgets(ttk.Frame):
	def __init__(self, parent):
		super().__init__(master = parent)
		# data
		self.time_window = TimeWindow(self).time_int.get()
		
		# add widgets
		
		self.widgets_timer = ttk.Meter(
				self,
				metersize = 300,
				amounttotal = 60,
				interactive = True,
				metertype = 'full',
				bootstyle = 'info',
				textright = 'S',
				meterthickness = 40,
				)
		
		self.play_button = ttk.Button(
				
				self,
				text = 'Play',
				command = self.play_button
				
				)
		
		self.cancel_button = ttk.Button(
				
				self,
				text = 'Cancel',
				command = self.cancel_button
				
				)
		# set layout
		
		self.widgets_timer.place(
				
				relx = 0.5,
				rely = 0.5,
				relheight = 0.8,
				relwidth = 0.8,
				anchor = 'center',
				
				)
		
		self.play_button.place(
				
				relx = 0.5,
				rely = 0.8,
				relwidth = 0.1,
				relheight = 0.15,
				anchor = 'center'
				
				)
		
		self.cancel_button.place(
				
				relx = 0.5,
				rely = 0.7,
				relwidth = 0.1,
				relheight = 0.15,
				anchor = 'center'
				
				)
	
	def play_button(self):
		pass
	
	def cancel_button(self):
		self.destroy()
	
	def retry_button(self):
		pass


class TimeWindow(ttk.Toplevel):
	
	def __init__(self, parent):
		super().__init__(master = parent)
		self.title('')
		left = int(self.winfo_screenwidth() / 2 - WIDTH_MIN / 2)
		top = int(self.winfo_screenheight() / 2 - HEIGHT_MIN / 2)
		self.geometry(f'{WIDTH_MIN}x{HEIGHT_MIN}+{left}+{top}')
		self.resizable(False, False)
		# style
		style = ttk.Style()
		
		style.configure('TLabel', font = ('Arial', 22))
		
		# variables
		self.time_int = ttk.IntVar()
		self.hour_int = ttk.IntVar(value = 0)
		self.minute_int = ttk.IntVar(value = 0)
		self.second_int = ttk.IntVar(value = 0)
		
		# add widgets
		
		self.hour_spinbox = ttk.Spinbox(
				self,
				from_ = 1,
				to = 24,
				textvariable = self.hour_int,
				wrap = True,
				width = 6,
				)
		
		self.space1 = ttk.Label(self, text = ":")
		self.space1.configure(anchor = 'n')
		
		self.spinbox = ttk.Spinbox(
				self,
				from_ = 0,
				to = 60,
				textvariable = self.minute_int,
				wrap = True,
				width = 6
				)
		self.minute_spinbox = self.spinbox
		
		self.space2 = ttk.Label(self, text = " : ")
		self.space2.configure(anchor = 'center')
		
		self.second_spinbox = ttk.Spinbox(
				self,
				from_ = 1,
				to = 60,
				textvariable = self.second_int,
				wrap = True,
				width = 6
				)
		# add buttons
		self.save_button = ttk.Button(
				self,
				text = 'Save',
				command = self.save_function
				)
		self.cancel_button = ttk.Button(
				self,
				text = 'Cancel',
				command = lambda: self.destroy()
				)
		
		# layout
		self.rowconfigure((0, 1), weight = 1, uniform = 'a')
		
		self.columnconfigure(0, weight = 1, uniform = 'a')
		self.columnconfigure(1, weight = 1, uniform = 'a')
		self.columnconfigure(2, weight = 1, uniform = 'a')
		self.columnconfigure(3, weight = 1, uniform = 'a')
		self.columnconfigure(4, weight = 1, uniform = 'a')
		
		self.hour_spinbox.grid(row = 0, column = 0, sticky = 'new')
		
		self.space1.grid(row = 0, column = 1, sticky = 'new')
		
		self.minute_spinbox.grid(row = 0, column = 2, sticky = 'new')
		
		self.space2.grid(row = 0, column = 3, sticky = 'new')
		
		self.second_spinbox.grid(row = 0, column = 4, sticky = 'new')
		
		#  set buttons
		self.save_button.grid(row = 1, column = 0, columnspan = 2, sticky = 'news')
		
		self.cancel_button.grid(row = 1, column = 3, columnspan = 2, sticky = 'news')
	
	def save_function(self):
		total_time = self.hour_int.get() * 3600 + self.minute_int.get() * 60 + self.second_int.get()
		self.time_int.set(total_time)
		if self.time_int.get() > 0:
			self.destroy()
			print(self.time_int.get())
	
	def cancel_function(self):
		self.destroy()
