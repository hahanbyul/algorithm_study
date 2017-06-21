# https://algospot.com/judge/problem/read/TIMETRIP

import math
import sys
input = sys.stdin.readline
import pprint as pp

class Timetrip:
    def __init__(self, G):
        self.G = G
        self.adj = {}

    def fill_graph(self, string):
        a, b, d = [int(i) for i in string.split()]
        if a not in self.adj.keys():
            self.adj[a] = []
        self.adj[a].append((b, d))

    def interpret(self, upper, opposite=False):
        if len(upper) > 0:
            shortest = upper[1]
        elif len(upper) == 0: # if negative cycle exists
            dist, via = self.floyd(opposite=opposite)
            shortest = dist[0][1]
            if self.has_cycle(via):
                return 'INFINITY'

        if shortest == math.inf:
            return 'UNREACHABLE'
        
        if opposite:
            return -shortest
        else:
            return shortest

    def solve(self):
        upper = self.bellmanFord()
        shortest = self.interpret(upper)
                
        lower = self.bellmanFord(opposite=True)
        longest = self.interpret(lower, opposite=True)

        if shortest == 'UNREACHABLE':
            print('UNREACHABLE')
            return shortest

        print('%s %s' % (str(shortest), str(longest)))
        return (shortest, longest)

    def floyd(self, opposite=False):
        V = self.G
        adj = [[math.inf for _ in range(V)] for _ in range(V)]

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

        upper = [math.inf for _ in range(V)]
        upper[src] = 0

        for _ in range(V):
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

        if updated:
            upper = []
        return upper


def main():
    C = int(input())
    for _ in range(C):
        G, W = [int(i) for i in input().split()]
        tt = Timetrip(G)
        for _ in range(W):
            tt.fill_graph(input())
        tt.solve()

if __name__ == '__main__':
    main()
