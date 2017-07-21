from PICNIC import Picnic

def test_read_friends():
    p = Picnic(2, 1)
    p.read_friends('0 1')
    assert p.relationship == [[0, 1], [1, 0]]

def test_memoization():
    dic = {}
    dic[[0,1]] = True

def test_baseline_condition():
    p = Picnic(2, 1)
    assert p.solve([0, 1]) == 1

    p = Picnic(4, 1)
    assert p.solve([0, 1, 2, 3]) == 1

def test_ex1():
    p = Picnic(2, 1)
    p.read_friends('0 1')
    assert p.solve([]) == 1

def test_ex2():
    p = Picnic(4, 6)
    p.read_friends('0 1 1 2 2 3 3 0 0 2 1 3')
    assert p.solve([]) == 3

def test_ex3():
    p = Picnic(6, 10)
    p.read_friends('0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5')
    assert p.solve([]) == 4
