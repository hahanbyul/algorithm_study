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

def test_is_in_board():
    assert not ex1.is_in_board(-1, 0)
    assert not ex1.is_in_board(2, 0)
    assert not ex1.is_in_board(-1, -1)
    assert ex1.is_in_board(0, 0)
    assert ex1.is_in_board(1, 1)

def test_solve():
    ex1.solve()

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
    
def test_on_random_input():
    N, M = 9, 9
    problem = choice(['L', 'R', 'U', 'D'], size=(N,M))
    problem[randint(0, N-1)][randint(0, M-1)] = '*'

    ex = COT()
    ex.N, ex.M = N, M
    ex.board = problem.tolist()
    ex.K = randint(N, N + M)
    ex.cache = [[[float('inf') for _ in range(ex.M)] for _ in range(ex.N)] for _ in range(ex.K+1)]
    # ex.K = randint(ex.min_dist(), ex.min_dist() + 3)

    print()
    print('%d %d %d' % (ex.N, ex.M, ex.K))
    ex.print_board(ex.board)

    ex.solve()

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

def test_sort_result():
    l1 = [(1,1,'R'), (0, 1, 'L')]
    l1.sort(key=lambda x: x[0]*10 + x[1])
    print(l1)
    a = {}
    a[''] = 1
    print(a[''])

