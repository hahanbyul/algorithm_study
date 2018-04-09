from FINDPATH import Findpath
import numpy as np

ex1 = Findpath(3)
for line in '0 1 0\n0 0 1\n1 0 0'.split('\n'):
    ex1.read_line(line)

ex2 = Findpath(7)
for line in '0 0 0 1 0 0 0\n0 0 0 0 0 0 1\n0 0 0 0 0 0 0\n0 0 0 0 1 1 0\n1 0 0 0 0 0 0\n0 0 0 0 0 0 1\n0 0 1 0 0 0 0'.split('\n'):
    ex2.read_line(line)

def test_graph():
    assert ex1.graph == [[0, 1, 0], [0, 0, 1], [1, 0, 0]]

def test_reachable():
    assert ex1.get_reachable() == [[float("inf"), 1, float("inf")], [float("inf"), float("inf"), 1], [1, float("inf"), float("inf")]]

def test_floyd():
    print()
    print(np.array(ex1.floyd()))

def test_solve():
    assert ex1.solve() == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    
def test_solve_ex2():
    answer = Findpath(7)
    for line in '1 0 1 1 1 1 1\n0 0 1 0 0 0 1\n0 0 0 0 0 0 0\n1 0 1 1 1 1 1\n1 0 1 1 1 1 1\n0 0 1 0 0 0 1\n0 0 1 0 0 0 0'.split('\n'):
        answer.read_line(line)

    assert ex2.solve() == answer.graph
