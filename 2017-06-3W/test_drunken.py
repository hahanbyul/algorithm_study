from DRUNKEN import Drunken
import pprint as pp

def test_ex():
    d = Drunken(8, 12, [8, 6, 5, 8, 3, 5, 8, 4])

def test_simple():
    d = Drunken(3, 3, [8, 5, 6])
    for w in '1 2 9\n1 3 3\n3 2 5'.split('\n'):
        d.fill_graph(w)

    d.floyd()

