import numpy as np

class TicTacToe:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.done = False
        self.winner = None
        return self.board.flatten()
    
    def is_winning(self, player):
        # Check rows, columns, and diagonals
        for i in range(3):
            if np.all(self.board[i, :] == player) or np.all(self.board[:, i] == player):
                return True
        if np.all(np.diag(self.board) == player) or np.all(np.diag(np.fliplr(self.board)) == player):
            return True
        return False
    
    def is_draw(self):
        return np.all(self.board != 0) and self.winner is None
    
    def step(self, action, player):
        row, col = divmod(action, 3)
        if self.board[row, col] == 0:
            self.board[row, col] = player
            if self.is_winning(player):
                self.done = True
                self.winner = player
            elif self.is_draw():
                self.done = True
                self.winner = 0
            return self.board.flatten(), self.done, self.winner
        else:
            return self.board.flatten(), False, self.winner
    
    def get_available_actions(self):
        return [i for i in range(9) if self.board.flatten()[i] == 0]
    
    def render(self):
        print(self.board)
