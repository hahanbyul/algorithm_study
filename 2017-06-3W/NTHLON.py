# https://algospot.com/judge/problem/read/NTHLON
import sys
import heapq
import math

# input = sys.stdin.readline

class Nthlon:
    def __init__(self):
        self.diff_plus, self.diff_minus, self.diff_zero = [ [] for _ in range(3) ]
        self.cost_plus, self.cost_minus, self.cost_zero = [ [] for _ in range(3) ]

    def read_record(self):
        record_str = input()
        record = record_str.split()
        A_time, B_time = int(record[0]), int(record[1])
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

    def diff(self, A, B):
        for A_time, B_time in zip(A, B):
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

    def solve(self):
        if len(self.diff_plus) * len(self.diff_minus) == 0:
            if len(self.diff_zero) == 0:
                return 'IMPOSSIBLE'
            else:
                return min(self.cost_zero)

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_plus, self.cost_plus)) ]
        heapq.heapify(frontier)
        discovered = {}
        #print(f'frontier: {frontier}')

        if len(self.cost_zero) > 0:
            max_limit = min(self.cost_zero)
        else:
            max_limit = 200*500

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)
            #print(f'[plus] cost: {cur_cost}, diff: {cur_diff}')

            answer = self.get_answer(cur_diff)
            if answer is not None:
                another_cost, another_diff = answer
                if cur_diff == another_diff:
                    return min(cur_cost + another_cost, max_limit)

            for i, (diff, cost) in enumerate(zip(self.diff_plus, self.cost_plus)):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if next_cost < max_limit and next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost

            #print(f'frontier: {frontier}')

    def get_answer(self, goal_diff):
        # TODO: 처음부터 시작하지 말고 이전에 하던 데부터...
        # if self.cache.get(goal_diff, False):
            #return self.cache[goal_diff]

        frontier = [ (cost, i, diff) for i, (diff, cost) in enumerate(zip(self.diff_minus, self.cost_minus)) if diff <= goal_diff ]
        if len(frontier) == 0:
            return

        heapq.heapify(frontier)
        discovered = {}
        #print(f'frontier: {frontier}')

        while len(frontier) > 0:
            cur_cost, current, cur_diff = heapq.heappop(frontier)
            #print(f'[minus] cost: {cur_cost}, diff: {cur_diff}')

            if goal_diff == cur_diff:
                return (cur_cost, cur_diff)

            for i, (diff, cost) in enumerate(zip(self.diff_minus, self.cost_minus)):
                next_cost = cur_cost + cost
                next_diff = cur_diff + diff

                if next_diff <= goal_diff and next_cost < discovered.get(next_diff, math.inf):
                    heapq.heappush(frontier, (next_cost, i, next_diff))
                    discovered[next_diff] = next_cost
            #print(f'frontier: {frontier}')

    def print_var(self):
        print(f'[self.diff] plus: {self.diff_plus}, zero: {self.diff_zero}, minus: {self.diff_minus}')
        print(f'[self.cost] plus: {self.cost_plus}, zero: {self.cost_zero}, minus: {self.cost_minus}')

def main():
    C = int(input())
    for _ in range(C):
        nthlon = Nthlon()

        M = int(input())
        for _ in range(M):
            nthlon.read_record()
        
        print(nthlon.solve())


if __name__ == '__main__':
    main()
