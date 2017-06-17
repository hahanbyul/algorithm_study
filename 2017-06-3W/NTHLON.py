# https://algospot.com/judge/problem/read/NTHLON
import sys
import heapq
import math

input = sys.stdin.readline

class Nthlon:
    def __init__(self):
        self.diff_plus, self.diff_minus, self.diff_zero = [ [] for _ in range(3) ]
        self.cost_plus, self.cost_minus, self.cost_zero = [ [] for _ in range(3) ]
        
        self.diff_plus_graph = None
        self.cache = {}

    def read_record(self):
        A_time, B_time = (int(t) for t in input().split())
        diff = A_time - B_time
        if diff > 0:
            self.diff_plus.append(diff)
            self.cost_plus.append(A_time)
        elif diff == 0:
            self.diff_zero.append(0)
            self.cost_zero.append(A_time)
        elif diff < 0:
            self.diff_minus.append(-diff)
            self.cost_minus.append(A_time)

    def make_graph(self):
        self.make_plus_graph()
        self.make_minus_graph()

    def make_plus_graph(self):
        self.diff_plus_graph = [self.diff_plus for _ in range(len(self.diff_plus))]
        self.cost_plus_graph = [self.cost_plus for _ in range(len(self.cost_plus))]

    def make_minus_graph(self):
        self.diff_minus_graph = [self.diff_minus for _ in range(len(self.diff_minus))]
        self.cost_minus_graph = [self.cost_minus for _ in range(len(self.cost_minus))]

    def solve(self):
        self.make_graph()

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_plus, self.cost_plus)) ]
        heapq.heapify(frontier)
        discovered = {}
        #print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)
            #print(f'[plus] cost: {cur_cost}, diff: {cur_diff}')

            another_cost, another_diff = self.get_answer(cur_diff)
            if cur_diff == another_diff:
                return cur_cost + another_cost

            for i, (diff, cost) in enumerate(zip(self.diff_plus_graph[current], self.cost_plus_graph[current])):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost

            #print(f'frontier: {frontier}')

    def get_answer(self, goal_diff):
        # TODO: 처음부터 시작하지 말고 이전에 하던 데부터...
        # if self.cache.get(goal_diff, False):
            #return self.cache[goal_diff]

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_minus, self.cost_minus)) ]
        if len(frontier) == 0:
            return math.inf, math.inf

        heapq.heapify(frontier)
        discovered = {}
        #print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)
            #print(f'[minus] cost: {cur_cost}, diff: {cur_diff}')

            if goal_diff <= cur_diff:
                return (cur_cost, cur_diff)

            for i, (diff, cost) in enumerate(zip(self.diff_minus_graph[current], self.cost_minus_graph[current])):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if next_diff <= goal_diff and next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost
            #print(f'frontier: {frontier}')

        return math.inf, math.inf

def main():
    C = int(input())
    for _ in range(C):
        M = int(input())

        nthlon = Nthlon()

        for _ in range(M):
            nthlon.read_record()

        if len(nthlon.diff_plus) * len(nthlon.diff_minus) == 0:
            print('IMPOSSIBLE')
            continue

        if max(nthlon.diff_plus) < max(nthlon.diff_minus):
            nthlon.diff_plus, nthlon.diff_minus = nthlon.diff_minus, nthlon.diff_plus
            nthlon.cost_plus, nthlon.cost_minus = nthlon.cost_minus, nthlon.cost_plus

        #print(f'[nthlon.diff] plus: {nthlon.diff_plus}, zero: {nthlon.diff_zero}, minus: {nthlon.diff_minus}')
        #print(f'[nthlon.cost] plus: {nthlon.cost_plus}, zero: {nthlon.cost_zero}, minus: {nthlon.cost_minus}')

        print()
        #print(nthlon.solve())


if __name__ == '__main__':
    main()
