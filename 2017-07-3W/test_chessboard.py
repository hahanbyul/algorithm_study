from FILL_CHESSBOARD import Board
import pprint as pp

def test_read():
    board = Board(8)
    for string in 'WBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW'.split('\n'):
        board.read_board(string)

def test_sum_total_fill():
    board = Board(4)
    assert board.sum_total_fill([1, 3, 0, 0]) == 1 + 1 + 4

def test_compute_next():
    board = Board(4)
    assert board.compute_next([1,3,0,0], list('WBWW'), list('BBBB')) == [2, 1, 3, 3]

def test_compute_next():
    board = Board(2)
    assert board.compute_next([1,1], list('BB'), list('BW')) == [1, 2]

def test_get_row_col():
    board = Board(4)
    for string in 'WBWW\nBBBB\nBBWW\nBWBB\nBBBB'.split('\n'):
        board.read_board(string)

    assert ''.join(board.get_row(0, 0)) == 'WBWW'
    assert ''.join(board.get_row(1, 0)) == 'BBBB'

    assert ''.join(board.get_col(0, 0)) == 'WBBB'
    assert ''.join(board.get_col(1, 0)) == 'BBBB'
    assert ''.join(board.get_col(0, 1)) == 'BBBW'

def test_howmany():
    board = Board(4)
    assert board.how_many(list('WBWW')) == 1
    assert board.how_many(list('BBBB')) == 2

def test_solve():
    board = Board(2)
    for string in 'WBWW\nBBBB\nBBWW\nBWBB\nBBBB'.split('\n'):
        board.read_board(string)

    pp.pprint(board.board)

    assert board.solve() == 0

def test_solve_ex():
    board = Board(8)
    for string in 'WBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBBBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW'.split('\n'):
        board.read_board(string)

    pp.pprint(board.board)

    assert board.solve() == 1


