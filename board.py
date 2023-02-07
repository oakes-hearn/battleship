class BoardManager:
    def __init__(self, board_size):
        self.board = []
        self.create_board(board_size)

    def create_board(self, board_size):
        board = [[' ' for x in range(0, board_size)] for x in range(0, board_size)]
        self.board = board

    def add_ship(self, length):
        # Assign ship type based on length
        match length:
            case 5:
                ship = "carrier"
            case 4:
                ship = "battleship"
            case 3:
                ship = "cruiser"
            case 2:
                ship = "submarine"
            case 1:
                ship = "destroyer"
        hor = None
        x_coor = None
        y_coor = None


        def determine_orientation():
            nonlocal hor
            # user selects orientation
            hor = input(f"Would you like the {ship} horizontal or vertical? (v/h): ").lower()
            if hor != 'h' and hor != 'v':
                print("Please enter 'v' for vertical or 'h' for horizontal.")
                determine_orientation()
                return
            hor = (hor == 'h')
            return

        def select_coordinates():
            nonlocal x_coor, y_coor
            # user selects starting coordinates 
            x = input(f"Which column would you like to place your {ship}?(0-9): ")
            y = input(f"Which row would you like to place your {ship}?(0-9): ")

            try:
                x = int(x)
                y = int(y)
            except ValueError or x > 9 or x < 0 or y > 9 or y < 0:
                print('Please enter valid integer coordinates.')
                select_coordinates()
            x_coor = x
            y_coor = y
            return
        determine_orientation()
        select_coordinates()

        # Check if ship is off board based on length and starting coordinates
        if (x_coor+length + 1 > len(self.board) and hor) or (y_coor+length + 1 > len(self.board) and not hor):
            print('Ship out of range of board. Please enter valid coordinates.')
            self.add_ship(length)
            return
        
        # Ensure not overlapping with placed ships
        if hor:
            for x in range(x_coor, x_coor+length+1):
                if self.board[y_coor][x] == 'o':
                    print('Overlaps with existing ships. Please enter valid coordinates.')
                    self.add_ship(length)
        else:
            for y in range(y_coor, y_coor+length+1):
                if self.board[y][x_coor] == 'o':
                    print('Overlaps with existing ships. Please enter valid coordinates.')
                    self.add_ship(length)

        # Place ship vertically or horizontally based on bool hor
        if hor:
            for x in range(x_coor, x_coor+length+1):
                self.board[y_coor][x] = 'o'
        else:
            for y in range(y_coor, y_coor+length+1):
                self.board[y][x_coor] = 'o'
        return 'Ship placed'