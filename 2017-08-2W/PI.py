# https://algospot.com/judge/problem/read/PI
import sys

class Pi:
    def __init__(self):
        self.cache = {}

    def dfs(self, picked, remained):
        if remained == 0:
            print(picked)
    
        for num_to_pick in [3, 4, 5]:
            next_remained = remained - num_to_pick
            if next_remained <= 2 and next_remained != 0:
                continue
            picked.append(num_to_pick)
            self.dfs(picked, next_remained)
            picked.pop()

    def solve(self, index):
        remained = len(self.string) - index
        if remained == 0:
            return 0

        if self.cache.get(index, False):
            return self.cache[index]

        ret = float('inf')
        for num_to_pick in [3, 4, 5]:
            next_remained = remained - num_to_pick
            if next_remained <= 2 and next_remained != 0:
                continue
            score = self.score(self.string[index:index+num_to_pick]) + self.solve(index + num_to_pick)
            ret = min(ret, score)

        self.cache[index] = ret
        return ret

    def score(self, pattern):
        # 3, 4, 5를 같이 계산하면 좀 빨리 계산할 수 있겠다
        array = [int(i) for i in pattern]
        diff_array = [array[i] - array[i+1] for i in range(len(array)-1)]
        odd_array = array[::2]
        even_array = array[1::2]

        if all([i == array[0] for i in array]):
            return 1
        elif all([i == 1 for i in diff_array]) or all([i == -1 for i in diff_array]):
            return 2
        elif all([i == odd_array[0] for i in odd_array]) and all([i == even_array[0] for i in even_array]):
            return 4
        elif all([i == diff_array[0] for i in diff_array]):
            return 5
        else:
            return 10


def main():
    C = int(input())
    for _ in range(C):
        pi = Pi()
        pi.string = input()
        # pi.string = sys.stdin.readline().split('\n')
        print(pi.solve(0))


if __name__ == '__main__':
    main()
