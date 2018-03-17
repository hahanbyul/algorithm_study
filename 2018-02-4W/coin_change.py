class CoinChange:
    def read_input_by(self, method):
        self.n, self.m = [int(x) for x in method().split()]
        self.c = [int(x) for x in method().split()]
        self.cache = [[-1 for _ in range(self.n+1)] for _ in range(self.m)]

    def solve(self):
        self.dfs(0, self.n, self.c)
        answer = self.cache[0][self.n]
        print(answer)
        return answer

    def dfs(self, start, remained, coin_list):
        cached_result = self.cache[start][remained]
        if cached_result != -1:
            return cached_result
            
        if remained == 0:
            return 1

        if remained < 0:
            return 0

        self.cache[start][remained] = 0
        for i in range(start, len(coin_list)):
            self.cache[start][remained] += self.dfs(i, remained - coin_list[i], coin_list)

        return self.cache[start][remained]

def main():
    cc = CoinChange()
    cc.read_input_by(input)
    cc.solve()

if __name__ == '__main__':
    main()
