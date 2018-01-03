from decomposition_reaction_dp import DecomReaction

def test_all_comb():
    dr = DecomReaction()
    # dr.all_comb(start=0, children_num=4, goal=5, summed=0, picked=[])
    dr.all_comb(start=0, children_num=1, goal=5, summed=0, picked=[])

dr = DecomReaction()
with open('ex_7_2.txt') as f:
    dr.read_input(f.readline)
dr.construct_tree()
dr.count_subtree()
print(dr.tree)
print(dr.subtree_count)

def test_solve_trivial_cases():
    assert dr.solve_with_root(1, 0) == 1
    assert dr.solve_with_root(2, 1) == 2

    assert dr.solve_without_root(1, 3) == float('inf')
    assert dr.solve_without_root(2, 3) == float('inf')

def test_solve():
    # assert dr.solve_without_root(0, 2) == 2
    # assert dr.solve_with_root(0, 2) == 3

    # assert dr.solve_without_root(0, 3) == 1
    # assert dr.solve_with_root(0, 3) == 2

    assert dr.solve_with_root(0, 4) == 1
    assert dr.solve_with_root(0, 5) == 2
    assert dr.solve_with_root(0, 6) == 1
    assert dr.solve_with_root(0, 7) == 0
