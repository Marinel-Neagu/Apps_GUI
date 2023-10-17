# size and layout app

APP_SIZE = (400, 700)
MAIN_ROW = 7
MAIN_COLUMN = 4

FONT = 'Helvetica'
OUTPUT_FONT_SIZE = 70
NORMAL_FONT_SIZE = 32
BUTTON_FONT_SIZE = 0

NUMBER_POSITIONS = {
		
		'0': {'row': 6, 'column': 0, 'span': 2},
		'.': {'row': 6, 'column': 2, 'span': 1},
		'1': {'row': 5, 'column': 0, 'span': 1},
		'2': {'row': 5, 'column': 1, 'span': 1},
		'3': {'row': 5, 'column': 2, 'span': 1},
		'4': {'row': 4, 'column': 0, 'span': 1},
		'5': {'row': 4, 'column': 1, 'span': 1},
		'6': {'row': 4, 'column': 2, 'span': 1},
		'7': {'row': 3, 'column': 0, 'span': 1},
		'8': {'row': 3, 'column': 1, 'span': 1},
		'9': {'row': 3, 'column': 2, 'span': 1},
		}
MATH_POSITIONS = {
		'=': {'row': 6, 'column': 3, 'character': '='},
		'+': {'row': 5, 'column': 3, 'character': '+', 'image_path': None},
		'-': {'row': 5, 'column': 3, 'character': '-', 'image_path': None},
		'X': {'row': 5, 'column': 3, 'character': 'X', 'image_path': None},
		'/': {'row': 5, 'column': 3, 'character': '/', 'image_path': None},
		}
MATH_OPERATORS = {
		'clear'  : {'row': 2, 'column': 0, 'span': 1, 'text': 'AC'},
		'invert' : {'row': 2, 'column': 1, 'span': 1, 'text': '+/-'},
		'percent': {'row': 2, 'column': 2, 'span': 1, 'text': '%'},
		}

GAP_SIZE = 0.5
TITLE_BAR_COLOR = {
		'dark' : 0x00000000,
		'light': 0xFFEEEE
		}
BLACK = '#000000'
WHITE = '#EEEEEE'
