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

ex3 = COT()
ex3.read_numbers('2 2 1')
ex3.read_board('RD\n*L')

ex4 = COT()
ex4.read_numbers('2 2 2')
ex4.read_board('DD\nU*')

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

def test_find_path_coord():
    assert ex1.find_path_coord('R') == (0,0)
    assert ex1.find_path_coord('RL') == (1,0)

def test_edit_and_recover_board():
    change = {(0,0): 'L', (0,1): 'R'}
    assert ex1.board_to_string(ex1.edit_board(change)) == 'LR*L'
    ex1.recover_board(change)
    assert ex1.board_to_string(ex1.board) == ex1.board_to_string(ex1.board_init)

def test_get_next_change():
    assert len(ex1.get_next_change({})) == 9

def test_list_add():
    assert ['a'] + ['b', 'c'] == ['a', 'b', 'c']
    a = ['a']
    a += ['b', 'c']

    assert a == ['a', 'b', 'c']

def test_solve_ex1():
    assert ex1.solve() == 0

def test_solve_ex3():
    assert ex3.solve() == 1

def test_solve_ex4():
    assert ex4.solve() == 1
