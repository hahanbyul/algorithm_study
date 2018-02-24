class CoinChange:
    def __init__(self):
        self.cache = {}

    def read_input_by(self, method):
        self.n, self.m = [int(x) for x in method().split()]
        self.c = [int(x) for x in method().split()]

    def solve(self):
        self.dfs(0, self.n, [])
        answer = self.cache[(0, self.n)]
        print(answer)
        return answer

    def dfs(self, start, remain, picked):
        if self.cache.get((start, remain), False):
            print('cached!!')
            return self.cache[(start, remain)]

        print(f'start: {start}, remain: {remain}')
        if remain == 0:
            print(f'picked: {picked}')
            return 1

        if remain < 0:
            return 0

        if start == self.m: # and remain > 0
            return 0

        for i in range(start, self.m):
            picked.append(self.c[i])
            self.cache[(start, remain)] = self.cache.get((start, remain), 0) + self.dfs(i, remain - self.c[i], picked)
            picked.pop()

        return self.cache[(start, remain)]


