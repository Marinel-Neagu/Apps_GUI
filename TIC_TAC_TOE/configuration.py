# size of the app

MAIN_SIZE = (800, 900)

# Layout BoardScore and BoardGame.
BOARD_SIZE = (3, 3)
BOARD_SCORE_SIZE = (9, 2)

# Style and attributes for widgets.


BOARD_GAME = {
        'FONT': 'Arial',
        'FONT_SIZE': 110,
        'BACKGROUND': '#1F1F1F',
        'HOVER_COLOR_ACTIVE': '#222222',
        'HOVER_COLOR_DISABLED': '#222222',
        'TEXT_COLOR_ACTIVE': '#E1D9D1',
        'TEXT_COLOR_DISABLED': '#E1D9D1',
        'BORDER_COLOR': '#121212',
        'BORDER_THICKNESS': 10,
        'BORDER_WIDTH': 2,
        'JUSTIFY': 'center',
        'RELIEF': 'solid',
        'PADX': 10,
        'PADY': 10,
        
        }
BOARD_SCORE = {
        
        'FONT': 'Helvetica',
        'FONT_SIZE': 34,
        'TEXT_COLOR': '#E1D9D1',
        'BACKGROUND_LABEL': '#303030',
        'BACKGROUND': '#121212',
        'PLAYER_1': {
                'row': 1,
                'col': 1,
                'columnspan': 3,
                },
        'PLAYER_2': {
                'row': 0,
                'col': 6,
                'columnspan': 3,
                },
        'TIE': {
                'row': 0,
                'col': 4,
                'columnspan': 2,
                },
        'RESET_BUTTON': {
                'row': 0,
                'col': 9,
                'columnspan': 3,
                'rowspan': 2,
                },
        'PLAYER_1_SCORE': {
                'row': 1,
                'column': 0,
                'columnspan': 3,
                },
        'TIE_SCORE': {
                'row': 1,
                'column': 4,
                'columnspan': 2,
                },
        'PLAYER_2_SCORE': {
                'row': 1,
                'column': 6,
                'columnspan': 3,
                },
        }
RESET_BUTTON = {
        'FONT': 'Helvetica',
        'SIZE': 34,
        'BACKGROUND': '#E74C3C',
        'HOVER_COLOR_ACTIVE': '#D95092',
        'HOVER_COLOR_DISABLED': '#E74C3C',
        'TEXT_COLOR_ACTIVE': '#E1D9D1',
        'TEXT_COLOR_DISABLED': '#E1D9D1',
        'BORDER_COLOR': '#222222',
        'BORDER_THICKNESS': 10,
        'BORDER_WIDTH': 2,
        'JUSTIFY': 'center',
        'RELIEF': 'solid',
        'PADX': 10,
        'PADY': 10,
        }
