from TRIPATHCNT import TriPath

board1 = [[1, -1, -1, -1], [1, 1, -1, -1], [1, 1, 1, -1], [1, 1, 1, 1]]
board2 = [[9, -1, -1, -1], [5, 7, -1, -1], [1, 3, 2, -1], [3, 5, 5, 6]]

def test_parse_board():
    tripath = TriPath(4, board1)

