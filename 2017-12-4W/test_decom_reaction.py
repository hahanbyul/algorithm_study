from decomposition_reaction import DecomReaction

dr_ex = DecomReaction()
with open('example.txt') as f:
    dr_ex.read_input(f.readline)

def test_read_input():
    dr = DecomReaction()
    dr.read_input(input)
    print(dr.connection)

def test_read_input_file():
    dr = DecomReaction()
    with open('example.txt') as f:
        dr.read_input(f.readline)
    print(dr.connection)

def test_count_connected():
    assert dr_ex.count_connected(1) == 8

def test_break_edge():
    assert dr_ex.break_edge_and_count_connected((1,3)) == (5, 3)
    assert dr_ex.break_edge_and_count_connected((1,2)) == (7, 1)
    assert dr_ex.break_edge_and_count_connected((6,1)) == (3, 5)

def test_solve():
    assert dr_ex.solve() == 1
    assert dr_ex.solve(1) == 1
    assert dr_ex.solve(2) == 2
    assert dr_ex.solve(3) == 1
    assert dr_ex.solve(4) == 2
    assert dr_ex.solve(6) == 2
    assert dr_ex.solve(7) == 1
    assert dr_ex.solve(8) == 0

def test_ex1():
    dr = DecomReaction()
    with open('ex1.txt') as f:
        dr.read_input(f.readline)
    assert dr.solve() == 2

def test_ex2():
    dr = DecomReaction()
    with open('ex2.txt') as f:
        dr.read_input(f.readline)
    assert dr.solve() == 1
    assert dr.solve(2) == 3
    assert dr.solve(3) == 3

def test_get_combinations():
    # dr_ex.get_combinations(0, [], 4, 8)
    dr_ex.get_combinations(0, [], 3, 6)

def test_opposite_end():
    dr3 = DecomReaction()
    with open('ex3.txt') as f:
        dr3.read_input(f.readline)

    assert dr3.opposite_end(0, 1) == 2
    assert dr3.opposite_end(0, 2) == 1
    assert dr3.opposite_end(4, 2) == 6

def test_ex3():
    dr3 = DecomReaction()
    with open('ex3.txt') as f:
        dr3.read_input(f.readline)
    dr3.solve3()

