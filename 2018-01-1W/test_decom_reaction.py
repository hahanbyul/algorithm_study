from decomposition_reaction_dp import DecomReaction

def test_all_comb():
    dr = DecomReaction()
    # dr.all_comb(start=0, children_num=4, goal=5, summed=0, picked=[])
    dr.all_comb(start=0, children_num=1, goal=5, summed=0, picked=[])

def test_construct_tree():
    dr = DecomReaction()
    with open('ex_7_2.txt') as f:
        dr.read_input(f.readline)

    dr.construct_tree()
    print(dr.tree)

    dr.count_subtree()
    print(dr.subtree_count)


