from minimum_budget import MinimumBudget

def test():
    mb = MinimumBudget()

    g[('A', 'B')] = 10
    g[('A', 'C')] = 30
    g[('A', 'D')] = 15
    g[('B', 'E')] = 20
    g[('E', 'F')] = 20
    g[('C', 'F')] = 5
    g[('D', 'C')] = 5
    g[('F', 'D')] = 20
    g[('D', 'F')] = 20

def test_bfs():
    graph = [[0,1,1,1,0,0],
             [0,0,0,0,1,0],
             [0,0,0,0,0,1],
             [0,0,1,0,0,1],
             [0,0,0,0,0,1],
             [0,0,0,1,0,0]]
    mb = MinimumBudget(1,1)
    mb.bfs(graph, 0)
