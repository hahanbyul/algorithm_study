from coin_on_the_table import CoinOnTheTable as COT
from pprint import pprint

def test_read_func():
    cot = COT()
    cot.read_numbers(input())

    board = []
    for n in range(cot.N):
        board.append(input())
    board_str = '\n'.join(board)
    cot.read_board(board_str)
    pprint(cot.board)

ex1 = COT()
ex1.read_numbers('2 2 3')
ex1.read_board('RD\n*L')

ex2 = COT()
ex2.read_numbers('4 4 5')
ex2.read_board('RDLU\nRDLU\nRDLU\nRRR*')

def test_find_star():
    assert ex1.find_star() == (1,0)
    assert ex2.find_star() == (3,3)

def test_min_dist():
    assert ex1.min_dist() == 1
    assert ex2.min_dist() == 6

def test_board_to_string():
    assert ex1.board_to_string(ex1.board) == 'RD*L'

def test_string_to_board():
    assert ex1.string_to_board('RD*L', 2, 2) == ex1.board

def test_find_path():
    assert ex1.find_path(ex1.board) == 'RDL'
    assert ex2.find_path(ex1.board) == 'RDDDRR'
