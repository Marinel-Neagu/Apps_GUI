from tkinter import IntVar

import ttkbootstrap as ttk
import sys, os
from widgets import BoardGame, BoardScore
from configuration import (
    
    # layout
    MAIN_SIZE,
    # style
    BOARD_GAME,
    BOARD_SCORE,
    RESET_BUTTON,
    )

# add the color title.(it works only on windows)
try:
    from ctypes import windll, byref, sizeof, c_int
except Exception:
    pass


def path_resource(relative_path: str) -> str:
    """
    it take the relative path and return the absolute path of the file from your system, is used for making the
    app into a exe file for window

    """
    try:
        base_path: str = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)


class TicTacToe(ttk.Window):
    player_1: IntVar
    tie_score: IntVar
    player_2: IntVar
    
    def __init__(self):
        super().__init__()
        self.bind('<Alt-s>', lambda event: self.destroy())
        self.title('')
        self.set_emtpy_icon()
        self.set_window_size(width = MAIN_SIZE[0], height = MAIN_SIZE[1])
        
        # set up the style
        self.Style = ttk.Style(theme = 'darkly')
        
        # style for the score/ board_score
        self.Style.configure(
                style = 'BoardScore.TFrame',
                background = BOARD_SCORE['BACKGROUND']
                )
        self.Style.configure(
                style = 'BoardGame.TFrame',
                background = BOARD_GAME['BACKGROUND']
                )
        self.Style.configure(
                style = 'BoardGame.TButton',
                font = (BOARD_GAME['FONT'], BOARD_GAME['FONT_SIZE']),
                background = BOARD_GAME['BACKGROUND'],
                bordercolor = BOARD_GAME['BORDER_COLOR'],
                borderthickness = BOARD_GAME['BORDER_THICKNESS'],
                borderwidth = BOARD_GAME['BORDER_WIDTH'],
                justify = BOARD_GAME['JUSTIFY'],
                relief = BOARD_GAME['RELIEF']
                )
        self.Style.map(
                style = 'BoardGame.TButton',
                foreground = [
                        ('active', BOARD_GAME['TEXT_COLOR_ACTIVE']),
                        ('disabled', BOARD_GAME['TEXT_COLOR_DISABLED'])
                        ],
                background = [
                        ('active', BOARD_GAME['HOVER_COLOR_ACTIVE']),
                        ('disabled', BOARD_GAME['HOVER_COLOR_DISABLED'])
                        ]
                )
        
        self.Style.configure(
                style = 'ResetButton.TButton',
                font = (RESET_BUTTON['FONT'], RESET_BUTTON['SIZE']),
                background = RESET_BUTTON['BACKGROUND'],
                bordercolor = RESET_BUTTON['BORDER_COLOR'],
                borderthickness = RESET_BUTTON['BORDER_THICKNESS'],
                borderwidth = RESET_BUTTON['BORDER_WIDTH'],
                justify = RESET_BUTTON['JUSTIFY'],
                relief = RESET_BUTTON['RELIEF']
                )
        self.Style.map(
                style = 'ResetButton.TButton',
                foreground = [
                        ('active', RESET_BUTTON['TEXT_COLOR_ACTIVE']),
                        ('disabled', RESET_BUTTON['TEXT_COLOR_DISABLED'])
                        ],
                background = [
                        ('active', RESET_BUTTON['HOVER_COLOR_ACTIVE']),
                        ('disabled', RESET_BUTTON['HOVER_COLOR_DISABLED'])]
                )
        
        self.Style.configure(
                style = 'BoardScore.TLabel',
                font = (BOARD_SCORE['FONT'], BOARD_SCORE['FONT_SIZE']),
                foreground = BOARD_SCORE['TEXT_COLOR'],
                background = BOARD_SCORE['BACKGROUND']
                )
        # 	set player data
        self.player_1 = ttk.IntVar(value = 0)
        self.tie_score = ttk.IntVar(value = 0)
        self.player_2 = ttk.IntVar(value = 0)
        
        # set widgets
        self.board_game = BoardGame(
                parent = self,
                style_cells = 'BoardGame.TButton',
                style_frame = 'BoardGame.TFrame',
                player_1 = self.player_1,
                tie = self.tie_score,
                player_2 = self.player_2,
                )
        self.board_score = BoardScore(
                parent = self,
                style_labels = 'BoardScore.TLabel',
                style_frame = 'BoardScore.TFrame',
                style_button = 'ResetButton.TButton',
                player_1 = self.player_1,
                tie = self.tie_score,
                player_2 = self.player_2,
                function = self.clean_board
                )
        
        # run
        self.mainloop()
    
    def clean_board(self):
        """
        It clean the board and reset the score
        """
        self.board_game.clean_board()
        self.player_1.set(0)
        self.player_2.set(0)
        self.tie_score.set(0)
    
    def set_emtpy_icon(self) -> None:
        """
        It sets the icon to  one empty from the title bar

        """
        try:
            path_image: str = path_resource('image/empty.ico')
            self.iconbitmap(path_image)
        except Exception:
            pass
    
    def set_window_size(self, width: int, height: int) -> None:
        """
        It adjust the window size to be in the center of the screen
        """
        left: int = int(self.winfo_screenwidth() / 2 - width / 2)
        top: int = int(self.winfo_screenheight() / 2 - height / 2)
        self.geometry(f'{width}x{height}+{left}+{top}')
    
    def set_title_bar_color(self) -> None:
        """
    It works only on Windows, not on GNU/Linux and macOS.
        """
        try:
            HWND: object = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE: int = 35
            TITLE_BAR_COLOR: int = 0x00000000
            windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_ATTRIBUTE, byref(c_int(TITLE_BAR_COLOR)), sizeof(c_int))
        except Exception:
            pass


if __name__ == '__main__':
    TicTacToe()
