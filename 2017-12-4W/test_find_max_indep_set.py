from find_max_indep_set import FindMaxIndepSet

ex_base = FindMaxIndepSet()
with open('example_base.txt') as f:
    ex_base.read_input(f.readline)

ex_online = FindMaxIndepSet()
with open('example_fmis_online.txt') as f:
    ex_online.read_input(f.readline)

def test_solve_base_case():
    assert solve(ex_base, 2, 1, False) == (0, [])
    assert solve(ex_base, 2, 1, True) == (10, [2])

    assert solve(ex_base, 3, 1, False) == (0, [])
    assert solve(ex_base, 3, 1, True) == (30, [3])

    assert solve(ex_base, 1, 0, False) == (40, [2, 3])
    assert solve(ex_base, 1, 0, True) == (20, [1])

def solve(obj, node, parent, is_included):
    obj.visited[parent] = True
    ans = obj.solve_(node, is_included) 
    obj.visited = [False for _ in range(obj.N+1)]
    print(obj.cache)
    return ans

def test_ex_base_solve():
    ex_base.solve()

def test_solve_base_case_online():
    # assert solve(ex_online, 5, 4, False) == (0, [])
    # assert solve(ex_online, 5, 4, True) == (20, [5])

    # assert solve(ex_online, 4, 3, False) == (20, [5])
    # assert solve(ex_online, 4, 3, True) == (10, [4])

    # assert solve(ex_online, 3, 2, False) == (20, [5])
    # assert solve(ex_online, 3, 2, True) == (60, [3, 5])

    # assert solve(ex_online, 6, 2, False) == (70, [7])
    # assert solve(ex_online, 6, 2, True) == (20, [6])

    assert solve(ex_online, 2, 1, False) == (130, [3, 5, 7])
    # assert solve(ex_online, 2, 1, True) == (60, [3, 5])

def test_ex_online_solve():
    ex_online.solve()
