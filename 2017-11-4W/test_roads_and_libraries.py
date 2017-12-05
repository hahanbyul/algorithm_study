from roads_and_libraries import RoadsAndLibraries

ral = RoadsAndLibraries()

def test_read_input():
    ral.read_input()

def test_true_plus():
    assert True + True == 2

def test_all_true():
    assert all([True, True])
    assert not all([False, True])

def test_compute_how_many_ex1():
    for i in [0, 1, 2]:
        print('i:', i+1)
        ex = RoadsAndLibraries()
        ex.read_input_file('ex1.txt')
        visited = [False for _ in range(ex.num_city)]
        assert ex.compute_how_many_cities_are_connected(i, visited) == 2

def test_compute_how_many_ex2():
    for i in [0, 1, 2, 3]:
        ex = RoadsAndLibraries()
        ex.read_input_file('ex2.txt')
        visited = [False for _ in range(ex.num_city)]
        assert ex.compute_how_many_cities_are_connected(i, visited) == 3

    for i in [4, 5]:
        ex = RoadsAndLibraries()
        ex.read_input_file('ex2.txt')
        visited = [False for _ in range(ex.num_city)]
        assert ex.compute_how_many_cities_are_connected(i, visited) == 1

def test_solve_ex1():
    ex = RoadsAndLibraries()
    ex.read_input_file('ex1.txt')
    assert ex.solve() == 4

def test_solve_ex2():
    ex = RoadsAndLibraries()
    ex.read_input_file('ex2.txt')
    assert ex.solve() == 12
