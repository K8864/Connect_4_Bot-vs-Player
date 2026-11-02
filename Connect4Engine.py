# In Connect4Engine.py
class Connect4Engine: 
    board = [['-' for _ in range(7)] for _ in range(6)] # 6 rows, 7 columns
    # player 1 uses x, player 2 uses o, - means not claimed
    player_bool = True # player 1 is true, player 2 is false.
    def __init__(self):
        pass

    def get_turn(self):
        return Connect4Engine.player_bool
    
    def set_turn(self, player):
        Connect4Engine.player_bool = player

    # plays a turn for player, returns the board after the turn if successful, raises ValueError if not
    def playTurn(self, player, column):
        if(player != Connect4Engine.player_bool):
            print("It's not your turn!")
            raise ValueError
        if(column < 0 or column > 6):
            print("Invalid column!")
            raise ValueError
        if(self.checkWin() != '-'):
            print("Game is already won by " + self.checkWin() + "!")
            raise ValueError
        for i in range(5, -1, -1):
            if(Connect4Engine.board[i][column] == '-'):
                Connect4Engine.board[i][column] = 'x' if player else 'o'
                Connect4Engine.player_bool = not Connect4Engine.player_bool
                return Connect4Engine.board
        raise ValueError
    
    # checks to see if any player has won
    def checkWin(self):
        for i in range(6):
            for j in range(7):
                if(Connect4Engine.board[i][j] != '-'):
                    if(j < 4 and Connect4Engine.board[i][j] == Connect4Engine.board[i][j+1] == Connect4Engine.board[i][j+2] == Connect4Engine.board[i][j+3]):
                        return Connect4Engine.board[i][j]
                    if(i < 3 and Connect4Engine.board[i][j] == Connect4Engine.board[i+1][j] == Connect4Engine.board[i+2][j] == Connect4Engine.board[i+3][j]):
                        return Connect4Engine.board[i][j]
                    if(i < 3 and j < 4 and Connect4Engine.board[i][j] == Connect4Engine.board[i+1][j+1] == Connect4Engine.board[i+2][j+2] == Connect4Engine.board[i+3][j+3]):
                        return Connect4Engine.board[i][j]
                    if(i < 3 and j > 2 and Connect4Engine.board[i][j] == Connect4Engine.board[i+1][j-1] == Connect4Engine.board[i+2][j-2] == Connect4Engine.board[i+3][j-3]):
                        return Connect4Engine.board[i][j]
        return '-'