# https://www.acmicpc.net/problem/1916
import math
import string
import heapq

class MinimumBudget:
    def __init__(self, n, m):
        self.city_num = n
        self.bus_num  = m

        self.budget = [[-1 for _ in range(n)] for _ in range(n)]

    def read_budget(self, input_str):
        here, there, budget = [int(x) for x in input_str.split()]
        current_budget = self.budget[here-1][there-1]
        if current_budget == -1 or current_budget > budget:
            self.budget[here-1][there-1] = budget

    def solve(self, here, there):
        return self.dijkstra(self.budget, here-1, there-1)

    def dijkstra(self, graph, start, goal):
        frontier = [ (0, start) ]
        discovered = {}

        while len(frontier) > 0:
            budget, current = heapq.heappop(frontier)
            if current == goal:
                return budget

            for i, edge in enumerate(graph[current]):
                next_budget = budget + edge
                if edge >= 0 and next_budget < discovered.get(i, math.inf):
                    heapq.heappush(frontier, (next_budget, i))
                    discovered[i] = next_budget


def main():
    n = int(input())
    m = int(input())

    mb = MinimumBudget(n, m)
    for _ in range(m):
        mb.read_budget(input())

    here, there = [int(x) for x in input().split()]
    print(mb.solve(here, there))


if __name__ == '__main__':
    main()
