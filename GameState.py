

class GameState:
    def __init__(self, board, turn_bool):
        self.board = board
        self.turn_bool = turn_bool
    
    def get_valid_moves(self):
        return [col for col in range(7) if self.board[0][col] == '-'] # column is playable if top row is empty, returns the indexes for all non-full columns
    
    def get_next_state(self): # returns a list of all possible next states for the current player
        next_states = []
        for col in self.get_valid_moves():
            new_board = [row[:] for row in self.board]
            for row in range(5, -1, -1):
                if new_board[row][col] == '-':
                    new_board[row][col] = 'x' if self.turn_bool else 'o'
                    break
            next_states.append(GameState(new_board, not self.turn_bool))
        return next_states