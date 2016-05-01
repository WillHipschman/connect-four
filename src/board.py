class Board(object):

    def __init__(self, width, height):
        self._num_cols = width
        self._num_rows = height
        self._board = [[0 for i in range(self._num_cols)] for j in range(self._num_rows)]

    def insert(self, col_num, player_id):

        if col_num > self._num_cols or col_num < 0:
            return False

        for i in range(self._num_rows - 1, -1, -1):
            if self._board[i][col_num] == 1 or self._board[i][col_num] == 2:
                continue
            else:
                self._board[i][col_num] = player_id
                return True
        return False

    def get_cell(self, row, col):
        return self._board[row][col]

    def print_board(self):
        for i in range(self._num_cols):
            print str(self._num_cols - i) + " " + " ".join(map(str, self._board[i]))
        print "  " + " ".join(map(str, range(1, self._num_cols + 1)))