from coin_on_the_table import CoinOnTheTable as COT
from pprint import pprint
from random import randint
from numpy.random import choice

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
ex2.read_board('RDLU\nRDDD\nRDRD\nRRR*')

ex3 = COT()
ex3.read_numbers('2 2 1')
ex3.read_board('RD\n*L')

ex4 = COT()
ex4.read_numbers('2 2 2')
ex4.read_board('DD\nU*')

ex5 = COT()
ex5.read_numbers('2 2 2')
ex5.read_board('DR\nU*')

ex6 = COT()
ex6.read_numbers('2 2 2')
ex6.read_board('LL\nL*')

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
    assert ex1.find_path() == (True, 'RDL')
    assert ex1.find_path(i=0,j=1) == (True, 'DL')
    assert ex1.find_path(i=1,j=1) == (True, 'L')
    assert ex1.find_path(i=1,j=0) == (True, '')

    assert ex2.find_path() == (True, 'RDDDRR')

    assert ex4.find_path() == (False, 'DU')
    assert ex4.find_path(i=1,j=0) == (False, 'UD')

def test_find_path_coord():
    assert ex1.find_path_coord('R') == (0,0)
    assert ex1.find_path_coord('RL') == (0,1)

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

def test_solve_ex5():
    assert ex5.solve() == 1

def test_solve_ex6():
    assert ex6.solve() == 2
    
def test_dict_keys():
    change = {(1,0): 'L', (0,1): 'R'}
    some_dict = {}
    some_dict[tuple(change.keys())] = 1
    print(some_dict)

def test_on_random_input():
    N, M = 4, 4
    problem = choice(['L', 'R', 'U', 'D'], size=(N,M))
    problem[randint(0, N-1)][randint(0, M-1)] = '*'

    ex = COT()
    ex.N, ex.M = N, M
    ex.board_init = problem.tolist()
    ex.board = problem.tolist()
    ex.K = randint(ex.min_dist(), N + M)
    # ex.K = randint(ex.min_dist(), ex.min_dist() + 3)

    print()
    print('%d %d %d' % (ex.N, ex.M, ex.K))
    ex.print_board(ex.board_init)

    ex.solve()

    print('======================================')
    print(ex.answer_change)
    ex.print_board(ex.answer_board)
    print(ex.answer_path)

def test_repeated_input():
    cot = COT()
    cot.read_numbers(input())

    board = []
    for n in range(cot.N):
        board.append(input())
    board_str = '\n'.join(board)
    cot.read_board(board_str)

    print()
    cot.solve()

    print('======================================')
    print(cot.answer_change)
    cot.print_board(cot.answer_board)
    print(cot.answer_path)

def test_new_path():
    path = ex2.find_path() 
    assert path == (True, 'RDDDRR')
    index = 2
    x, y = ex2.find_path_coord(path[1][:index+1])
    assert x == 1 and y == 1
    ex2.board[x][y] = 'R'
    assert path[:index+1] + ex2.find_path(i=x,j=y)[1] == 'RDRDRD'
