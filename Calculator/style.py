from settings import *
import ttkbootstrap as ttk

ttk.Style().configure('Result.TLabel', font = (FONT, OUTPUT_FONT_SIZE))
ttk.Style().configure('Formula.TLabel', font = (FONT, NORMAL_FONT_SIZE))
ttk.Style().configure(
		'Number.TButton',
		font = (FONT, NORMAL_FONT_SIZE),
		borderwidth = 5,
		bordercolor = 'black',
		)
ttk.Style().configure(
		'Operators.TButton',
		font = (FONT, NORMAL_FONT_SIZE),
		borderwidth = 0,
		background = '#F0AD4E',
		fg_color = 'red'
		)
ttk.Style().configure(
		'Symbols.TButton',
		font = (FONT, NORMAL_FONT_SIZE),
		background = '#4E5D6C',
		borderwidth = 0,
		activebackground = 'red'
		)
