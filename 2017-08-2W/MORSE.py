# https://algospot.com/judge/problem/read/MORSE

class Morse:
    def __init__(self):
        self.factorial_cache = {}

    def factorial(self, N):
        if self.factorial_cache.get(N, False):
            return self.factorial_cache[N]

        if N == 1 or N == 0:
            return 1

        ret = N * self.factorial(N-1)
        self.factorial_cache[N] = ret
        return ret

    def get_comb_num(self, n_dash, n_circle):
        # problematic!!!!!! (big int)
        return self.factorial(n_dash + n_circle) // self.factorial(n_dash) // self.factorial(n_circle)

    def solve(self, n_dash, n_circle, ith_num):
        if n_dash == 0 and n_circle == 0:
            return ''
        if n_dash == 0 and n_circle > 0:
            return 'o' * n_circle

        possible_comb = self.get_comb_num(n_dash-1, n_circle)
        if ith_num > possible_comb:
            return 'o' + self.solve(n_dash, n_circle-1, ith_num - possible_comb)
        else:
            return '-' + self.solve(n_dash-1, n_circle, ith_num)

    def print_all_cases(self, n_dash, n_circle):
        for i in range(self.get_comb_num(n_dash, n_circle)):
            print(self.solve(n_dash, n_circle, i+1))


def main():
    C = int(input())
    morse = Morse()
    for _ in range(C):
        n, m, k = [int(i) for i in input().split()]
        print(morse.solve(n, m, k))


if __name__ == '__main__':
    main()
