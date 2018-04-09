from GALLERY import Gallery

ex1 = '0 1\n1 2\n1 3\n2 5\n0 4'

def test_read_edge():
    g = Gallery(6, 5)
    g.read_graph_as_string(ex1)

def test_solve():
    g = Gallery(6, 7)
    g.read_graph_as_string('0 1\n0 2\n0 3\n0 4\n3 4\n4 5\n3 5')
    g.solve()

def test_ex1():
    g = Gallery(6, 5)
    g.read_graph_as_string(ex1)
    g.solve()

def test_ex2():
    g = Gallery(4, 2)
    g.read_graph_as_string('0 1\n2 3')
    g.solve()

def test_ex3():
    g = Gallery(1000, 1)
    g.read_graph_as_string('0 1')
    g.solve()

