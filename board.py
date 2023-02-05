from pandas import DataFrame

class BoardManager:
    def __init__(self, board_size):
        self.board = []
        self.create_board(board_size)

    def create_board(self, board_size):
        board = [[' ' for x in range(0, board_size+1)] for x in range(0, board_size+1)]
        self.board = board

    def add_ship(self, x_coor, y_coor, length, hor=True):
        # Check if ship is off board based on length and starting (x,y)
        if (x_coor+length > len(self.board) and hor) or (y_coor+length > len(self.board) and not hor):
            return 'ship out of range of board'
        
        # Ensure not overlapping with placed ships
        if hor:
            for x in range(x_coor, x_coor+length+1):
                if self.board[y_coor][x] == 'o':
                    return 'Overlaps with existing ships'
        else:
            for y in range(y_coor, y_coor+length+1):
                if self.board[y][x_coor] == 'o':
                    return 'Overlaps with existing ships'
        
        # Place ship vertically or horizontally based on bool hor
        if hor:
            for x in range(x_coor, x_coor+length+1):
                self.board[y_coor][x] = 'o'
        else:
            for y in range(y_coor, y_coor+length+1):
                self.board[y][x_coor] = 'o'
        return 'Ship placed'

board = BoardManager(10)
print(board.add_ship(1, 0, 3, hor=True))
print(board.add_ship(1,2, 5, hor=True))
print(board.add_ship(8, 3, 3, hor=False))
print(board.add_ship(2, 4, 2, hor=False))
print(board.add_ship(4, 5, 4, hor=False))
print(board.add_ship(1, 0, 3, hor=False))
print(DataFrame(board.board))
