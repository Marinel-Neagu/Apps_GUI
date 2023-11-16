import ttkbootstrap as ttk
from configuration import BOARD_SIZE


class BoardGame(ttk.Frame):
    
    def __init__(
            self, parent, style_cells, style_frame,
            player_1, tie, player_2, ):
        super().__init__(master = parent, style = style_frame)
        # set data
        self.player_1 = player_1
        self.tie_score = tie
        self.player_2 = player_2
        self.x_score = 0
        self.o_score = 0
        self.t_score = 0
        self.players_list = ['X', 'O']
        self.player = self.players_list[0]
        self.board_position = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                ]
        # layout
        
        self.columnconfigure(list(range(BOARD_SIZE[0])), weight = 1, uniform = 'a')
        self.rowconfigure(list(range(BOARD_SIZE[1])), weight = 1, uniform = 'a')
        self.pack(expand = True, fill = 'both', side = 'top')
        
        #  add the buttons
        for rows in range(BOARD_SIZE[0]):
            for cols in range(BOARD_SIZE[1]):
                self.board_position[rows][cols] = Button(
                        parent = self,
                        text = '',
                        command = lambda row = rows, column = cols: self.player_move(row, column),
                        row = rows,
                        column = cols,
                        style_button = style_cells,
                        columnspan = 1,
                        rowspan = 1,
                        )
    
    def player_move(self, row: int, column: int) -> None:
        """
        It updates the board when the player click the cells and is the hole logic for the board

        """
        if self.board_position[row][column]['text'] == "" and self.check_win() is False:
            self.round(row = row, column = column)
        else:
            if self.empty_space() or self.check_win():
                self.clean_board()
    
    def round(self, row: int, column: int) -> None:
        """
         It check the round if it is X or O round and
        check the round if is done and update the score
        
        """
        
        # The first move is always for the X player
        
        if self.player == self.players_list[0]:
            self.round_x(row = row, column = column)
        else:
            self.round_o(row = row, column = column)
    
    def round_x(self, row: int, column: int) -> None:
        """
        Update the board and the score for the X  player
        
        """
        self.board_position[row][column]['text'] = self.player
        if self.check_win() is False:
            self.player = self.players_list[1]
        
        elif self.check_win() is True:
            
            self.player_1.set(self.player_1.get() + 1)
        
        elif self.check_win() == "Tie":
            
            self.tie_score.set(self.tie_score.get() + 1)
    
    def round_o(self, row: int, column: int) -> None:
        """
        
        Update the board and the score for the O  player

        """
        self.board_position[row][column]['text'] = self.player
        
        if self.check_win() is False:
            
            self.player = self.players_list[0]
        
        elif self.check_win() is True:
            
            self.player_2.set(self.player_2.get() + 1)
        
        elif self.check_win() == "Tie":
            
            self.tie_score.set(self.tie_score.get() + 1)
    
    def check_win(self):
        # Check for winning conditions
        if self.row_check() or self.column_check():
            return True
        
        elif self.check_first_diagonal() or self.check_second_diagonal():
            return True
        
        elif self.empty_space():
            return 'Tie'
        else:
            return False
    
    def column_check(self):
        for column in range(BOARD_SIZE[1]):
            
            if self.board_position[0][column]['text'] == self.board_position[1][column]['text'] == \
                    self.board_position[2][column]['text'] != "":
                
                return True
    
    def row_check(self):
        for row in range(BOARD_SIZE[0]):
            
            if self.board_position[row][0]['text'] == self.board_position[row][1]['text'] == \
                    self.board_position[row][2]['text'] != "":
                
                return True
    
    def check_first_diagonal(self):
        
        if self.board_position[0][0]['text'] == self.board_position[1][1]['text'] == \
                self.board_position[2][2]['text'] != "":
            
            return True
    
    def check_second_diagonal(self):
        
        if self.board_position[0][2]['text'] == self.board_position[1][1]['text'] == \
                self.board_position[2][0]['text'] != "":
            
            return True
    
    def empty_space(self):
        
        spaces = 9
        
        for row in range(BOARD_SIZE[0]):
            for column in range(BOARD_SIZE[1]):
                
                if self.board_position[row][column]['text'] != '':
                    spaces -= 1
        
        return True if spaces == 0 else False
    
    def clean_board(self):
        # Clear the button texts and backgrounds
        for row in range(BOARD_SIZE[0]):
            for column in range(BOARD_SIZE[1]):
                self.board_position[row][column]['text'] = ''


class BoardScore(ttk.Frame):
    
    def __init__(
            self,
            parent,
            style_labels,
            style_frame,
            player_1,
            tie,
            player_2,
            function,
            style_button,
            
            ):
        super().__init__(master = parent, style = style_frame)
        # data score
        self.player_1_score = player_1
        self.player_2_score = player_2
        self.tie_score = tie
        
        self.columnconfigure(list(range(10)), weight = 1, uniform = 'b')
        self.rowconfigure((0, 1), weight = 1, uniform = 'b')
        self.pack(fill = 'both', side = 'bottom')
        
        # show players name
        self.player_1 = Label(
                parent = self,
                text = 'Player X',
                row = 0,
                column = 0,
                columnspan = 3,
                style = style_labels,
                )
        self.tie = Label(
                parent = self,
                text = 'Tie ',
                row = 0,
                column = 4,
                columnspan = 2,
                style = style_labels,
                )
        
        self.player_2 = Label(
                parent = self,
                text = 'Player O',
                row = 0,
                column = 6,
                columnspan = 3,
                style = style_labels,
                )
        self.reset_button = Button(
                parent = self,
                text = 'Reset\nGame',
                command = function,
                row = 0,
                column = 9,
                columnspan = 3,
                rowspan = 2,
                style_button = style_button,
                
                )
        # show score
        self.label_player_1_score = LabelScore(
                parent = self,
                textvariable = self.player_1_score,
                row = 1,
                column = 0,
                columnspan = 3,
                style = style_labels,
                
                )
        
        self.label_tie_score = LabelScore(
                parent = self,
                textvariable = self.tie_score,
                row = 1,
                column = 4,
                columnspan = 2,
                style = style_labels,
                )
        self.label_player_2_score = LabelScore(
                parent = self,
                textvariable = self.player_2_score,
                row = 1,
                column = 6,
                columnspan = 3,
                style = style_labels,
                )


class Button(ttk.Button):
    
    def __init__(
            self, parent, text, command,
            row, column, columnspan, rowspan, style_button,
            ):
        # set data
        super().__init__(
                master = parent,
                text = text,
                command = command,
                style = style_button,
                )
        
        # set layout
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                rowspan = rowspan,
                padx = 5,
                pady = 5
                )


class Label(ttk.Label):
    def __init__(self, parent, text, row, column, columnspan, style, ):
        super().__init__(
                master = parent,
                text = text,
                style = style,
                anchor = 'center',
                )
        
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                padx = 10,
                pady = 10,
                )


class LabelScore(ttk.Label):
    def __init__(self, parent, textvariable, row, column, columnspan, style):
        super().__init__(
                master = parent,
                textvariable = textvariable,
                style = style,
                anchor = 'center',
                )
        self.grid(
                row = row,
                column = column,
                sticky = 'news',
                columnspan = columnspan,
                padx = 10,
                pady = 10
                )
