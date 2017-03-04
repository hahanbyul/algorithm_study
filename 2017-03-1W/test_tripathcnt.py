from TRIPATHCNT import TriPath

board1 = [[1, -1, -1, -1], [1, 1, -1, -1], [1, 1, 1, -1], [1, 1, 1, 1]]
board2 = [[9, -1, -1, -1], [5, 7, -1, -1], [1, 3, 2, -1], [3, 5, 5, 6]]

def test_parse_board():
    tripath = TriPath(4, board1)

def test_base_condition():
    tripath = TriPath(4, board2)
    assert tripath.path(3,3) == 6

def test_max_path():
    tripath = TriPath(4, board2)
    assert tripath.path(2,2) == 8
    assert tripath.path(0,0) == 24

    tripath2 = TriPath(4, board1)
    assert tripath2.path(0,0) == 4

def test_cache():
    tripath = TriPath(4, board2)
    tripath.path(0,0)
    assert tripath.cache[0][0] == 24
    print(tripath.cache)


