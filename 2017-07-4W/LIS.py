class LIS:
    def __init__(self):
        self.cache = {}

    def read_seq(self, string):
        self.seq = [int(i) for i in string.split()]

    def solve(self):
        ret = 0
        for i in range(len(self.seq)):
            ret = max(ret, self.lis(i))

        return ret

    def lis(self, start):
        if self.cache.get(start, False):
            return self.cache[start]

        ret = 1
        for i in range(start+1, len(self.seq)):
            if self.seq[i] > self.seq[start]:
                ret = max(ret, 1 + self.lis(i))

        self.cache[start] = ret
        return ret


def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        lis = LIS()
        lis.read_seq(input())
        print(lis.solve())


if __name__ == '__main__':
    main()
            


