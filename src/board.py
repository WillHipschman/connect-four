class Board(object):

    def __init__(self, width, height):
        self._width = width
        self._heigiht = height
        board = [[0 for i in range(0, width)] for j in range(0, height)]

    def insert(self, board, col_num, height, player_id):
        for i in range(self._height, 0):
            if self._board[col_num, i] == 1 or self._board[col_num, i] == 2:
                continue
            else:
                self._board[col_num, i] = player_id
                return True
        return False

    def get_cell(self, row, col):
        return self._board[row, col]


