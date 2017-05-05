from SEP_AREA import Separated_area

problem = Separated_area()
problem.read_problem("5 7 3")
problem.read_rect("0 2 4 4")
problem.read_rect("1 1 2 5")
problem.read_rect("4 0 6 2")

def test_fill_rect():
    assert problem.board == [[0,0,0,0,1,1,0],[0,1,0,0,1,1,0],[1,1,1,1,0,0,0],[1,1,1,1,0,0,0],[0,1,0,0,0,0,0]]

def test_dfs():
    ex = Separated_area()
    ex.board = [[0,1],
                [0,0]]
    ex.M = 2
    ex.N = 2
    assert ex.dfs(0,0) == 3

def test_ex():
    problem.solve()
