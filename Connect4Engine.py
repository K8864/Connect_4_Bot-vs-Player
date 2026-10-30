"""
TODO
Finish the game logic
Implement a UI for the connect 4 game
Implement a depth limited minimax algorithm with alpha beta pruning to play against the player
"""

# A Connect 4 board is 7 columns x 6 grids
# I'll use a 2d array to represent a board
class Connect4: 
    board = [['-' for _ in range(7)] for _ in range(6)] # 6 rows, 7 columns
    # player 1 uses x, player 2 uses o, - means not claimed
    player_bool = True # player 1 is true, player 2 is false.
    def __init__():
        pass

    def get_turn():
        return Connect4.player_bool

    # plays a turn for player, returns the board after the turn if successful, raises ValueError if not
    def playTurn(player, column):
        if(player != Connect4.player_bool):
            print("It's not your turn!")
            raise ValueError
        if(column < 0 or column > 6):
            print("Invalid column!")
            raise ValueError
        if(Connect4.checkWin() != '-'):
            print("Game is already won by " + Connect4.checkWin() + "!")
            raise ValueError
        for i in range(0, 5):
            if(Connect4.board[i][column] == '-'):
                Connect4.board[i][column] = 'x' if player else 'o'
                Connect4.player_bool = not Connect4.player_bool
                return Connect4.board
        return ValueError
    
    # checks to see if any player has won
    def checkWin():
        for i in range(6):
            for j in range(7):
                if(Connect4.board[i][j] != '-'):
                    if(j < 4 and Connect4.board[i][j] == Connect4.board[i][j+1] == Connect4.board[i][j+2] == Connect4.board[i][j+3]):
                        return 'x' if Connect4.player_bool else 'o'
                    if(i < 3 and Connect4.board[i][j] == Connect4.board[i+1][j] == Connect4.board[i+2][j] == Connect4.board[i+3][j]):
                        return 'x' if Connect4.player_bool else 'o'
                    if(i < 3 and j < 4 and Connect4.board[i][j] == Connect4.board[i+1][j+1] == Connect4.board[i+2][j+2] == Connect4.board[i+3][j+3]):
                        return 'x' if Connect4.player_bool else 'o'
                    if(i < 3 and j > 2 and Connect4.board[i][j] == Connect4.board[i+1][j-1] == Connect4.board[i+2][j-2] == Connect4.board[i+3][j-3]):
                        return 'x' if Connect4.player_bool else 'o'
        return '-'
    
