from decomposition_reaction_dfs import DecomReaction

def test_example(filename):
    dr = DecomReaction()
    with open(filename) as f:
        dr.read_input(f.readline)

    node, parent = 0, -1
    dr.dfs(node, parent)
    print(f'without: {dr.min_cut_without_root[node]}')
    print(f'with: {dr.min_cut_with_root[node]}')

def test_7_2():
    test_example('ex_7_2.txt')

def test_online_ex():
    test_example('example.txt')

def test_online_ex_1():
    test_example('ex_1.txt')

def test_online_ex_2():
    test_example('ex_2.txt')
