from TIMETRIP import Timetrip
import pprint as pp

def test_ex1():
    tt = Timetrip(2)
    for w in '0 1 1\n0 1 3'.split('\n'):
        tt.fill_graph(w)

    solution = tt.solve()
    assert solution == (1,3)

def test_ex2():
    tt = Timetrip(4)
    for w in '0 2 -7\n0 3 -4\n3 2 9\n2 1 3'.split('\n'):
        tt.fill_graph(w)

    solution = tt.solve()
    assert solution == (-4,8)

def test_ex3():
    tt= Timetrip(4)
    for w in '0 2 0\n2 2 1\n2 1 0'.split('\n'):
        tt.fill_graph(w)

    solution = tt.solve()
    assert solution == (0,'INFINITY')

def test_minus_cycle():
    tt = Timetrip(2)
    for w in '0 1 -1\n1 0 -3'.split('\n'):
        tt.fill_graph(w)
    solution = tt.solve()

def test_ex4_no_path():
    tt = Timetrip(3)

    solution = tt.solve()
    assert solution == 'UNREACHABLE'

def test_floyd():
    tt= Timetrip(4)
    for w in '0 2 0\n2 2 -1\n2 1 0'.split('\n'):
        tt.fill_graph(w)

    dist, via = tt.floyd()
    assert tt.has_cycle(via) == True

def test_minus_cycle2():
    tt= Timetrip(4)
    for w in '0 0 -2\n0 3 1\n2 3 1\n3 2 2\n2 1 0'.split('\n'):
        tt.fill_graph(w)

    dist, via = tt.floyd()
    print(via)
    assert tt.has_cycle(via) == True

    solution = tt.solve()
    assert solution == ('INFINITY','INFINITY')
