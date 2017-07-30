class LIS:
    def __init__(self):
        self.cache = {}
        self.max_val = 0

    def solve(self, seq):
        for i, num in enumerate(seq):
            ret = self.cache.get(i, False)
            if not ret:
                ret = self.max_length(seq[i:], 0, i)
                self.cache[i] = ret
            self.max_val = max(self.max_val, ret)

        print(self.max_val)
        return self.max_val

    def max_length(self, seq, num, index):
        if self.cache.get(index, False):
            return self.cache[index]

        if len(seq) == 0:
            return 0

        if seq[0] <= num:
            return self.max_length(seq[1:], num, index+1)
        else:
            ret = 0
            for i in range(len(seq)):
                ret = max(ret, 1 + self.max_length(seq[i+1:], seq[0], index+i+1))
            self.cache[index] = ret
            return ret


def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        lis = LIS()

        seq = [int(i) for i in input().split()]
        lis.solve(seq)


if __name__ == '__main__':
    main()
            


