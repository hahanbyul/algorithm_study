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

    def solve(self):
        upper = self.bellmanFord()
        print(f'upper: {upper}')
        if len(upper) > 0:
            shortest = upper[1]
        elif len(upper) == 0: # if negative cycle exists
            dist = self.floyd()
            print(dist)
            shortest = dist[0][1]
            if dist[0][0] < 0 and shortest != math.inf:
                shortest = 'INFINITY'

        if shortest == math.inf:
            return 'UNREACHABLE'
                
        lower = self.bellmanFord(opposite=True)
        if len(lower) > 0:
            longest = -lower[1]
        elif len(lower) == 0:
            dist = self.floyd(opposite=True)
            print(dist)
            longest = -dist[0][1]
            if dist[0][0] < 0 and longest != math.inf:
                longest = 'INFINITY'

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
        pp.pprint(adj)

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    print(f'({k},{i},{j})')
                    if adj[i][j] > adj[i][k] + adj[k][j]:
                        adj[i][j] = adj[i][k] + adj[k][j]
                        pp.pprint(adj)
        return adj

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
