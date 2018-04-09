from KEVIN_BACON import KevinBacon
import pprint as pp

def test_floyd():
    kb = KevinBacon(5)
    for string in '1 3\n1 4\n4 5\n4 3\n3 2'.split('\n'):
        kb.connect(string)

    kb.solve()
