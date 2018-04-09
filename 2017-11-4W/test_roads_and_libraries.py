from roads_and_libraries import RoadsAndLibraries

ral = RoadsAndLibraries()

def test_read_input():
    ral.read_input()

def test_true_plus():
    assert True + True == 2

def test_all_true():
    assert all([True, True])
    assert not all([False, True])

def test_solve_ex1():
    ex = RoadsAndLibraries()
    ex.read_input_file('ex1.txt')
    assert ex.solve() == 4

def test_solve_ex2():
    ex = RoadsAndLibraries()
    ex.read_input_file('ex2.txt')
    assert ex.solve() == 12
