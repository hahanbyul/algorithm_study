from KLIS import KLIS

def test_ex1():
    lis = KLIS()
    lis.read_seq('5 1 6 4 3 2 8 7')
    lis.solve(6)

def test_ex1():
    lis = KLIS()
    lis.read_seq('2 1 4 3 6 5 8 7')
    lis.solve(4)

def test_ex3():
    lis = KLIS()
    lis.read_seq('5 6 7 8 1 2 3 4')
    lis.solve(2)
