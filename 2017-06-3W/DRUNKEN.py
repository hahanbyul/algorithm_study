import pprint as pp

class Drunken:
    def __init__(self, V, E, V_cost):
        self.V = V
        self.E = E
        self.V_cost = V_cost

        self.adj = [[-1 for _ in range(V)] for _ in range(V)]

    def fill_graph(self, string):
        A, B, C = [int(i) for i in string.split()]
        self.adj[A-1][B-1] = C
        self.adj[B-1][A-1] = C

    def floyd(self):
        V = self.V
        adj = [[float("inf") for _ in range(V)] for _ in range(V)]

        for here in range(V):
            for there, cost in enumerate(self.adj[here]):
                if adj[here][there] > cost:
                    adj[here][there] = cost

        for i in range(V):
            adj[i][i] = 0
        # pp.pprint(adj)

        via = [[-1 for _ in range(V)] for _ in range(V)]

        cost = [[-1 for _ in range(V)] for _ in range(V)]

        V_cost = self.V_cost
        for i in range(V):
            for j in range(V):
                cost[i][j] = max(V_cost[i], V_cost[j])

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    max_cost = max(cost[i][k], cost[k][j])
                    print(f'({i},{j}): {adj[i][j]} ({cost[i][j]}) / ({i},{k}): {adj[i][k]}, ({k},{j}): {adj[k][j]} ({max_cost})')
                    if adj[i][j] + cost[i][j] > adj[i][k] + adj[k][j] + max_cost:
                        adj[i][j] = adj[i][k] + adj[k][j]
                        via[i][j] = k
                        cost[i][j] = max(cost[i][j], max_cost)
                        # pp.pprint(adj)

        pp.pprint(adj)
        pp.pprint(cost)
        return (adj, via)

def main():
    V, E = [int(i) for i in input().split()]
    V_cost = [int(i) for i in input().split()]

    d = Drunken(V, E, V_cost)
    for _ in range(E):
        d.fill_graph(input())

    T = int(input())
    for _ in range(T):
        s, t = [int(i) for i in input().split()]


if __name__ == '__main__':
    main()
