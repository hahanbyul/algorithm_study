# https://www.acmicpc.net/problem/1389
import pprint as pp

class KevinBacon:
    def __init__(self, V):
        self.V = V
        self.network = [[float('inf') for _ in range(V)] for _ in range(V)]

    def connect(self, string):
        src, target = [int(i) for i in string.split(' ')]
        self.network[src-1][target-1] = 1
        self.network[target-1][src-1] = 1

    def floyd(self):
        V = self.V

        adj = [[float('inf') for _ in range(V)] for _ in range(V)]

        for here in range(V):
            for there, cost in enumerate(self.network[here]):
                adj[here][there] = cost
                if here == there:
                    adj[here][there] = 0

        via = [[-1 for _ in range(V)] for _ in range(V)]

        for k in range(V):
            for i in range(V):
                for j in range(V):
                    if adj[i][j] > adj[i][k] + adj[k][j]:
                        adj[i][j] = adj[i][k] + adj[k][j]
                        via[i][j] = k

        return adj

    def solve(self):
        adj = self.floyd()
        stage_sum = [sum(row) for row in adj]

        answer = stage_sum.index(min(stage_sum)) + 1
        print(answer)
        return answer


def main():
    N, M = [int(i) for i in input().split(' ')]
    kb = KevinBacon(N)
    for _ in range(M):
        kb.connect(input())

    kb.solve()



if __name__ == '__main__':
    main()
