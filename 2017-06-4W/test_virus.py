from VIRUS import Virus

def test_bfs():
    v = Virus(7)
    for edge in '1 2\n2 3\n1 5\n5 2\n5 6\n4 7'.split('\n'):
        v.connect(edge)

    assert v.solve() == 4
