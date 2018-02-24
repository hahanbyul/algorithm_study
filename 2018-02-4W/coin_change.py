class CoinChange:
    def __init__(self):
        self.answer = 0

    def read_input_by(self, method):
        self.n, self.m = [int(x) for x in method().split()]
        self.c = [int(x) for x in method().split()]

    def solve(self):
        self.dfs(0, 0, [])
        print(self.answer)
        return self.answer

    def dfs(self, start, sum_picked, picked):
        print(f'start: {start}, sum_picked: {sum_picked}, picked: {picked}')
        if sum_picked == self.n:
            self.answer += 1
            print('answer!!')
            return

        if sum_picked > self.n:
            return

        if start == self.m:
            return

        for i in range(start, self.m):
            picked.append(self.c[i])
            self.dfs(i, sum_picked + self.c[i], picked)
            picked.pop()

