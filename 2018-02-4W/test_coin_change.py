from coin_change import CoinChange

def get_problem(index):
    cc = CoinChange()
    with open(f'prob1_ex{index}.txt') as f:
        cc.read_input_by(f.readline)
    return cc

def test_read_by_input_function():
    cc = CoinChange()
    cc.read_input_by(input)
    print(cc.n)

def test_solve_for_ex1():
    ex1 = get_problem(1)
    print(ex1.c)
    assert ex1.solve() == 4

def test_solve_for_ex2():
    ex2 = get_problem(2)
    print(ex2.c)
    assert ex2.solve() == 5

def test_solve_for_ex3():
    ex3 = get_problem(3)
    print(ex3.c)
    assert ex3.solve() == 4


