# https://www.acmicpc.net/problem/1916
import string
import heapq

class MinimumBudget:
    def __init__(self, n, m):
        self.city_num = n
        self.bus_num  = m
        self.budget = dict()

    def read_budget(self, input_str):
        begin_city, end_city, budget = [int(x) for x in input_str.split()]
        self.budget[(begin_city, end_city)] = budget

    def solve(self, here, there):
        pass 

    def bfs(self, graph, start):
        frontier = [ start ]
        visited  = {}

        while len(frontier) > 0:
            current = frontier.pop(0)
            print(f'current: {string.ascii_uppercase[current]}')

            for i, edge in enumerate(graph[current]):
                if edge and not visited.get(i, False):
                    frontier.append(i)
                    visited[i] = True



def main():
    n = int(input())
    m = int(input())

    mb = MinimumBudget(n, m)
    for _ in range(m):
        mb.read_budget(input())

    here, there = [int(x) for x in input().split()]
    mb.solve(here, there)


if __name__ == '__main__':
    main()
