from TIMETRIP import Timetrip

def test_ex1():
    tt = Timetrip(2)
    for w in '0 1 1\n0 1 3'.split('\n'):
        print(w)
        tt.fill_graph(w)
    print(tt.adj)
    print(tt.solve())

def test_ex2():
    tt = Timetrip(4)
    for w in '0 2 -7\n0 3 -4\n3 2 9\n2 1 3'.split('\n'):
        print(w)
        tt.fill_graph(w)
    print(tt.adj)
    print(tt.solve())

def test_ex3():
    tt= Timetrip(4)
    for w in '0 2 0\n2 2 1\n2 1 0'.split('\n'):
        tt.fill_graph(w)
    print(tt.adj)
    print(tt.solve())

def test_minus_cycle():
    tt = Timetrip(2)
    for w in '0 1 -1\n1 0 -3'.split('\n'):
        tt.fill_graph(w)
    print(tt.adj)
    print(tt.solve())

def test_no_path():
    tt = Timetrip(3)
    print(tt.adj)
    print(tt.solve())

