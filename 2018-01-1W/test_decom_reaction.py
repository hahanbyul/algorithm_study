from decomposition_reaction_dp import DecomReaction

def test_all_comb():
    dr = DecomReaction()
    # dr.all_comb(start=0, children_num=4, goal=5, summed=0, picked=[])
    dr.all_comb(start=0, children_num=1, goal=5, summed=0, picked=[])
