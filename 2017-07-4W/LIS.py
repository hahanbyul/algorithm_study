class LIS:
    def __init__(self):
        self.cache = {}
        self.choices = {}

    def read_seq(self, string):
        self.seq = [int(i) for i in string.split()]

    def solve(self):
        return self.lis(-1)-1

    def lis(self, start):
        if self.cache.get(start, False):
            return self.cache[start]

        ret = 1
        for i in range(start+1, len(self.seq)):
            if start == -1 or self.seq[i] > self.seq[start]:
                ans = 1 + self.lis(i)
                if ret < ans:
                    ret = ans
                    self.choices[start] = i

        self.cache[start] = ret
        return ret

    def reconstruct(self):
        return self.reconstruct_(self.choices[-1], [])

    def reconstruct_(self, start, seq):
        print("start: %d, seq: %s" % (start, seq))
        seq.append(self.seq[start])
        if start not in self.choices.keys():
            return seq
        return self.reconstruct_(self.choices[start], seq)


def main():
    C = int(input())
    for _ in range(C):
        N = int(input())
        lis = LIS()
        lis.read_seq(input())
        print(lis.solve())


if __name__ == '__main__':
    main()
            


