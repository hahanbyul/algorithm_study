# https://algospot.com/judge/problem/read/FESTIVAL
import pprint as pp


class Festival:
    def __init__(self, price, L, N):
        self.lst = price
        self.L = L
        self.N = N

        self.cache = dict()

    def solve(self):
        self.sum_init()

        lowest_mean = self.mean(self.L)
        for i in range(self.L+1, self.N+1):
            self.sum_using_cache(i)
            mean = self.mean(i)
            if mean < lowest_mean:
                lowest_mean = mean

        return lowest_mean
        # pp.pprint(self.cache)

    def sum_init(self):
        self.cache[self.L] = self.sum_n(self.lst, self.L)

    def mean(self, k):
        return float(min(self.cache[k])) / k

    def sum_n(self, lst, n):
        sum_list = list()
        sum_list.append(sum(lst[:n]))
        for i in range(len(lst)-n):
            sum_list.append(sum_list[-1] - lst[i] + lst[i+n])

        self.cache[n] = self.cache
        return sum_list

    def sum_using_cache(self, n):
        sum_n_minus_1 = self.cache[n-1]
        sum_n = list()
        for i, prev in enumerate(sum_n_minus_1[:-1]):
            sum_n.append(prev + self.lst[i+n-1])

        self.cache[n] = sum_n
        return sum_n


def main():
    C = int(input())
    for _ in range(C):
        N, L = [int(i) for i in input().split()]
        price = [int(i) for i in input().split()]
        
        f = Festival()
        print(f.solve(price, N))


if __name__ == '__main__':
    main()
