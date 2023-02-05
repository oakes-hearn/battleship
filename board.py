class BoardManager:
    def __init__(self, board_size):
        self.board = []
        self.create_board(board_size)

    def create_board(self, board_size):
        row = []
        board = []
        for i in range(0, board_size+1):
            row.append(' ')
        for i in range(0, board_size+1):
            board.append(row)
        self.board = board
        

board = BoardManager(10)
