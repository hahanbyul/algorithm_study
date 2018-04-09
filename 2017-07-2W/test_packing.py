from PACKING import Packing

ex1 = 'laptop 4 7\ncamera 2 10\nxbox 6 6\ngrinder 4 7\ndumbell 2 5\nencyclopedia 10 4'

def test_read_line():
    p = Packing(10)
    for line in ex1.split('\n'):
        p.read_line(line)

    print(p.thing_list)
    p.thing_list.sort(key=lambda tup: -tup[2])
    print(p.thing_list)

def test_dfs():
    p = Packing(10)
    for line in ex1.split('\n'):
        p.read_line(line)

    p.thing_list.sort(key=lambda tup: tup[1])
    p.dfs([], 0, 0, 0)

def test_solve():
    p = Packing(10)
    for line in ex1.split('\n'):
        p.read_line(line)

    assert p.solve() == (24, 3)

def test_ex2_solve():
    p = Packing(17)
    for line in ex1.split('\n'):
        p.read_line(line)

    assert p.solve() == (30, 4)

def test_solve_memo():
    p = Packing(17)
    for line in ex1.split('\n'):
        p.read_line(line)
    p.thing_list.sort(key=lambda tup: tup[1]) # sort by volume
    print(p.thing_list)
    assert p.solve_memo(10, 0) == 24
    assert p.solve_memo(17, 0) == 30

