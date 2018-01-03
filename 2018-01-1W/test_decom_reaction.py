from decomposition_reaction_dp import DecomReaction

def test_all_comb():
    dr = DecomReaction()
    # dr.all_comb(start=0, children_num=4, goal=5, summed=0, picked=[])
    dr.all_comb(start=0, children_num=1, goal=5, summed=0, picked=[])

dr = DecomReaction()
with open('ex_7_2.txt') as f:
    dr.read_input(f.readline)

def test_construct_tree():
    dr.construct_tree()
    print(dr.tree)

    dr.count_subtree()
    print(dr.subtree_count)

def test_solve_trivial_cases():
    dr.construct_tree()
    dr.count_subtree()
    print(dr.tree)
    print(dr.subtree_count)

    # cut <= 1 
    assert dr.solve(3,1) == 1

    # tree_size < cut
    assert dr.solve(1,4) == float('inf')

    # tree_size == cut
    assert dr.solve(1,3) == 1
    assert dr.solve(2,3) == 1

    # tree_size == cut-1
    assert dr.solve(1,2) == 1

def test_solve_trivial_cases():
    dr.construct_tree()
    dr.count_subtree()
    print(dr.tree)
    print(dr.subtree_count)

    # assert dr.solve(0, 1) == 1

    # assert dr.solve(1, 2) == 2
    # assert dr.solve(2, 3) == 1
    assert dr.solve(0, 2) == 2

    # assert dr.solve(0, 4) == 1
    # assert dr.solve(0, 5) == 2
