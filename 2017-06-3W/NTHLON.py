# https://algospot.com/judge/problem/read/NTHLON
import sys
import heapq

input = sys.stdin.readline

class Nthlon:
    def lin_comb(self, diff_arr, cost_arr):
        diff_graph = [diff_arr for _ in range(len(diff_arr))]
        cost_graph = [cost_arr for _ in range(len(cost_arr))]
        max_limit = 100

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(diff_arr, cost_arr)) ]
        heapq.heapify(frontier)
        visited = {}
        print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)

            if cur_cost > max_limit:
                return 

            print(cur_cost)
            for i, (diff, cost) in enumerate(zip(diff_graph[current], cost_graph[current])):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if not visited.get(next_diff, False):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    visited[next_diff] = True
            #print(f'frontier: {frontier}')

    def get_answer(self, diff_arr, cost_arr, goal_diff):
        cost_arr = [cost for cost, diff in zip(cost_arr, diff_arr) if diff <= goal_diff]
        diff_arr = [diff for diff in diff_arr if diff <= goal_diff]
        print(f'diff: {diff_arr}')
        print(f'cost: {cost_arr}')



def main():
    C = int(input())
    for _ in range(C):
        M = int(input())
        for _ in range(M):
            A_time, B_time = (int(t) for t in input().split())


if __name__ == '__main__':
    main()
