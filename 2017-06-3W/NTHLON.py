# https://algospot.com/judge/problem/read/NTHLON
import sys
import heapq
import math

input = sys.stdin.readline

class Nthlon:
    def lin_comb(self, max_limit):
        diff_graph = [self.diff_plus for _ in range(len(self.diff_plus))]
        cost_graph = [self.cost_plus for _ in range(len(self.cost_plus))]

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_plus, self.cost_plus)) ]
        heapq.heapify(frontier)
        discovered = {}
        print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)

            if cur_cost > max_limit:
                return 

            print(cur_cost)
            for i, (diff, cost) in enumerate(zip(diff_graph[current], cost_graph[current])):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost

            #print(f'frontier: {frontier}')

    def get_answer(self, goal_diff):
        self.cost_minus = [cost for cost, diff in zip(self.cost_minus, self.diff_minus) if diff <= goal_diff]
        self.diff_minus = [diff for diff in self.diff_minus if diff <= goal_diff]

        diff_graph = [self.diff_minus for _ in range(len(self.diff_minus))]
        cost_graph = [self.cost_minus for _ in range(len(self.cost_minus))]

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_minus, self.cost_minus)) ]

        heapq.heapify(frontier)
        discovered = {}
        print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)
            print(cur_cost)

            if goal_diff <= cur_diff:
                return cur_cost

            for i, (diff, cost) in enumerate(zip(diff_graph[current], cost_graph[current])):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                print(f'[next] cost: {next_cost}, diff: {next_diff}')

                if next_diff <= goal_diff and next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost
            print(f'frontier: {frontier}')

def main():
    C = int(input())
    for _ in range(C):
        M = int(input())

        diff_plus, diff_minus, diff_zero = [ [] for _ in range(3) ]
        cost_plus, cost_minus, cost_zero = [ [] for _ in range(3) ]

        for _ in range(M):
            A_time, B_time = (int(t) for t in input().split())
            diff = A_time - B_time
            if diff > 0:
                diff_plus.append(diff)
                cost_plus.append(A_time)
            elif diff == 0:
                diff_zero.append(0)
                cost_zero.append(A_time)
            elif diff < 0:
                diff_minus.append(-diff)
                cost_minus.append(A_time)

        print(f'[diff] plus: {diff_plus}, zero: {diff_zero}, minus: {diff_minus}')
        print(f'[cost] plus: {cost_plus}, zero: {cost_zero}, minus: {cost_minus}')

        if len(diff_plus) * len(diff_minus) == 0:
            print('IMPOSSIBLE')
            continue


if __name__ == '__main__':
    main()
