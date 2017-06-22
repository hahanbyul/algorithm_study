from DRUNKEN import Drunken
import pprint as pp

def test_ex():
    d = Drunken(8, 12, [8, 6, 5, 8, 3, 5, 8, 4])
    for w in '1 6 9\n1 2 3\n2 8 3\n6 8 5\n6 7 3\n8 7 3\n6 5 5\n4 5 7\n3 4 4\n3 5 2\n2 3 6\n7 5 1'.split('\n'):
        d.fill_graph(w)

    pp.pprint(d.adj)
    pp.pprint(d.V_cost)
    assert d.solve(1, 5) == 17
    pp.pprint(d.adj)
    pp.pprint(d.V_cost)
    assert d.solve(6, 3) == 10


def test_simple():
    d = Drunken(3, 3, [8, 5, 6])
    for w in '1 2 9\n1 3 3\n3 2 5'.split('\n'):
        d.fill_graph(w)
