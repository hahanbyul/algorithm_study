from coin_change import CoinChange

cc = CoinChange()
with open('prob1_ex.txt') as f:
    cc.read_input_by(f.readline)

cc2 = CoinChange()
with open('prob1_ex2.txt') as f:
    cc2.read_input_by(f.readline)

def test_read_by_input_function():
    cc = CoinChange()
    cc.read_input_by(input)
    print(cc.n)

def test_solve_for_ex1():
    cc.solve()

def test_solve_for_ex2():
    cc2.solve()
