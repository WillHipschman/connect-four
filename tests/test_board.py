import Board

class TestBoard():

    def test_insert(self):
        width = 8
        height = 8

        board = Board(width = width, height = height)
        for i in range(0, width - 1):
            for j in range(0, height - 1):
                assert board.get_cell(i, j) == 0