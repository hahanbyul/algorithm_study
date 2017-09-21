from equal import Equal

def test_sub_min():
    assert Equal.sub_min([1, 2, 3, 4]) == [0, 1, 2, 3]
    assert Equal.sub_min([1, 3, 3, 3]) == [0, 2, 2, 2]

def test_add():
    assert Equal.add([1, 2, 3, 4], 2, 3) == [3, 4, 5, 4]

def test_all_same():
    assert Equal.are_all_same([0] * 4)
    assert not Equal.are_all_same([0, 1, 2, 3])

def test_solve_exit():
    eq = Equal([0] * 4)
    assert eq.solve(eq.array) == 0

def test_solve_ex():
    eq = Equal([2, 2, 3, 7])
    assert eq.solve(eq.array) == 2

def test_solve_ex():
    eq = Equal([2, 2, 3, 7])
    assert eq.solve_bfs() == 2
