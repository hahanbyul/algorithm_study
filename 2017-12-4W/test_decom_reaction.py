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
