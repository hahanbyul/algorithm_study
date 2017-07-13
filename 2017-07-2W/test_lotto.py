from LOTTO import Lotto

def test_read_line():
    l = Lotto()
    l.read_line('7 1 2 3 4 5 6 7')
    assert l.S == ['1', '2', '3', '4', '5', '6', '7']

def test_solve():
    l = Lotto()
    l.read_line('7 1 2 3 4 5 6 7')
    l.solve()

def test_solve2():
    l = Lotto()
    l.read_line('8 1 2 3 5 8 13 21 34')
    l.solve()

