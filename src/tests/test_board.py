from src.board import Board

width = 8
height = 8

def _create_and_validate_board(columns_to_insert, expected_positions):
    board = Board(width = width, height = height)

    for col in columns_to_insert:
        result = board.insert(col, player_id=1)
        assert  result == (col < width and col >= 0)

    for i in range(0, width - 1):
        for j in range(0, height - 1):
            if (i,j) in expected_positions:
                assert board.get_cell(i, j) == 1
            else:
                assert board.get_cell(i, j) == 0


def test_insert_into_board():
    _create_and_validate_board(
        columns_to_insert = [1, 1, 1, 1, 1, 1, 1, 1],
        expected_positions=[(7, 1), (6, 1), (5, 1), (4, 1), (3,1), (2,1), (1,1), (0, 1)])
    _create_and_validate_board(
        columns_to_insert = [1, 1, 1, 1],
        expected_positions=[(7, 1), (6, 1), (5, 1), (4, 1)])
    _create_and_validate_board(
        columns_to_insert = [1, 2, 3, 4],
        expected_positions=[(7, 1), (7, 2), (7, 3), (7, 4)])
    _create_and_validate_board(
        columns_to_insert = [1, 1, 2, 3],
        expected_positions=[(7, 1), (6, 1), (7, 2), (7, 3)])
    _create_and_validate_board(
        columns_to_insert = [1, 3, 5, 7],
        expected_positions=[(7, 1), (7, 3), (7, 5), (7, 7)])
    _create_and_validate_board(
        columns_to_insert = [-1, 1000, 1, 1],
        expected_positions=[(7, 1), (6, 1)])


def test_new_board_is_empty():
    _create_and_validate_board(columns_to_insert = [], expected_positions=[])
