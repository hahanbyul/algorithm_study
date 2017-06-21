# https://algospot.com/judge/problem/read/TIMETRIP

import pprint as pp

class Timetrip:
    def __init__(self, G):
        self.G = G
        self.adj = {}

    def fill_graph(self, string):
        a, b, d = [int(i) for i in string.split(' ')]
        if a not in self.adj.keys():
            self.adj[a] = []
        self.adj[a].append((b, d))

    def solve(self):
        shortest = self.bellmanFord()
        longest = self.bellmanFord(opposite=True)

        if shortest == float('inf') or longest == float('inf'):
            print('UNREACHABLE')
            return 'UNREACHABLE'

        print('%s %s' % (str(shortest), str(longest)))
        return (shortest, longest)

    def floyd(self, opposite=False):
        V = self.G
        adj = [[float("inf") for _ in range(V)] for _ in range(V)]

        for here in self.adj.keys():
            for there, cost in self.adj[here]:
                if opposite:
                    cost = -cost

                if adj[here][there] > cost:
                    adj[here][there] = cost

        for i in range(V):
            if adj[i][i] > 0:
                adj[i][i] = 0
        # pp.pprint(adj)

        via = [[-1 for _ in range(V)] for _ in range(V)]

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    # print(f'({k},{i},{j})')
                    if adj[i][j] > adj[i][k] + adj[k][j]:
                        adj[i][j] = adj[i][k] + adj[k][j]
                        via[i][j] = k
                        # pp.pprint(adj)

        return (adj, via)

    def has_cycle(self, via):
        mid = via[0][1]
        return via[0][0] == 0 or via[1][1] == 1 or via[mid][mid] == mid

    def bellmanFord(self, src=0, opposite=False):
        V = self.G

        upper = [float("inf") for _ in range(V)]
        upper[src] = 0

        for _ in range(V-1):
            updated = False
            for here in range(V):
                for there, cost in self.adj.get(here, []):
                    if opposite:
                        cost = -cost

                    if upper[there] > upper[here] + cost:
                        upper[there] = upper[here] + cost
                        updated = True

            if not updated:
                break

        for here in range(V):
            for there, cost in self.adj.get(here, []):
                if opposite:
                    cost = -cost

                if upper[there] > upper[here] + cost:
                    reachable, via = self.floyd(opposite=opposite)
                    if reachable[0][here] != float('inf') and reachable[here][1] != float('inf'):
                        return 'INFINITY'

        if opposite:
            return -upper[1]
        else:
            return upper[1]


def main():
    C = int(input())
    for _ in range(C):
        G, W = [int(i) for i in input().split(' ')]
        tt = Timetrip(G)
        for _ in range(W):
            tt.fill_graph(input())
        tt.solve()

if __name__ == '__main__':
    main()
