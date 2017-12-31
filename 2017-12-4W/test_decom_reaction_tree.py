from decomposition_reaction_tree import DecomReaction

def test_read_input():
    dr = DecomReaction()
    with open('example.txt') as f:
        dr.read_input(f.readline)
    dr.solve()

def test_find_min_sum_():
    dr = DecomReaction()
    print([5, 4, 3, 1, 1, 1])
    assert dr.find_min_sum_(array=[5, 4, 3, 1, 1, 1], start=0, goal=7, cache={}) == 3
    assert dr.find_min_sum_(array=[5, 4, 3, 1, 1, 1], start=1, goal=7, cache={}) == 2

def test_find_min_sum():
    dr = DecomReaction()
    assert dr.find_min_sum(array=[5, 4, 3, 1, 1, 1], goal=7) == 2


def test_read_input():
    dr = DecomReaction()
    with open('ex_decom_answer_4.txt') as f:
        dr.read_input(f.readline)
    assert dr.solve() == 2
