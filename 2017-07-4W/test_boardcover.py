from BOARDCOVER import Boardcover
import pprint as pp

def test_read_board():
    bc = Boardcover()
    bc.read_board(3, 7)

def test_read_board():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##...##'.split('\n'):
        bc.read_line(line)

    assert bc.board == [[1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 1, 1]]

def test_is_full():
    bc = Boardcover()
    print('\n#######\n#.....#\n##...##')
    for line in '#######\n#.....#\n##...##'.split('\n'):
        bc.read_line(line)

    assert bc.is_full_row(0)
    assert bc.is_full_col(0)
    assert bc.is_full_col(6)

def test_print_board():
    bc = Boardcover()
    for line in '########\n#..##..#\n##.##.##'.split('\n'):
        bc.read_line(line)

    bc.print_board(bc.board)

def test_cut_board():
    bc = Boardcover()
    for line in '#####\n##.##\n##.##\n#####'.split('\n'):
        bc.read_line(line)

    assert bc.cut_board(bc.board) == [[0], [0]]

def test_solve():
    bc = Boardcover()
    for line in '########\n#..##..#\n##.##.##'.split('\n'):
        bc.read_line(line)

    print()
    assert bc.solve(bc.board) == 1

def test_ex0():
    bc = Boardcover()
    for line in '##.##..\n#......\n#....##\n#..####'.split('\n'):
        bc.read_line(line)

    print()
    assert bc.is_solvable(bc.board)
    bc.solve(bc.board)

def test_ex1():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##...##'.split('\n'):
        bc.read_line(line)

    print()
    assert bc.solve(bc.board) == 0
    assert not bc.is_solvable(bc.board)
    bc.print_cache()

def test_ex2():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##..###'.split('\n'):
        bc.read_line(line)

    print()
    assert bc.solve(bc.board) == 2
    assert bc.is_solvable(bc.board)
    bc.print_cache()

def test_ex3():
    bc = Boardcover()
    for line in '##########\n#........#\n#........#\n#........#\n#........#\n#........#\n#........#\n##########'.split('\n'):
        bc.read_line(line)

    print()
    assert bc.solve(bc.board) == 1514
    
def test_fill():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##...##'.split('\n'):
        bc.read_line(line)

    board = bc.cut_board(bc.board)
    print()
    bc.print_board(board)

    board_ = bc.fill_board(board, 'L')
    bc.print_board(board_)
    assert bc.is_full_col(board_, 0)
    assert not bc.is_full_col(board_, 1)

    bc.print_board(bc.fill_board(board, 'L_90'))
    bc.print_board(bc.fill_board(board, 'L_180'))
    bc.print_board(bc.fill_board(board, 'L_270'))

def test_count_zero():
    bc = Boardcover()
    assert bc.count_zero([[1, 0], [0, 0]]) == 3

def test_is_solvable():
    bc = Boardcover()

    assert not bc.is_solvable([[0, 0]])
    assert bc.is_solvable([[1, 0], [0, 0]])

def test_to_string_and_to_board():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##...##'.split('\n'):
        bc.read_line(line)

    assert bc.to_string(bc.board) == '#.....#\n#.....#\n##...##'
    assert bc.to_board('#.....#\n#.....#\n##...##') == bc.board

def test_memoization():
    bc = Boardcover()
    for line in '#.....#\n#.....#\n##..###'.split('\n'):
        bc.read_line(line)

    bc.solve(bc.board)
    bc.print_cache()

