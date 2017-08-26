class KLIS:
    def __init__(self):
        self.cache = {}
        self.choices = {}

    def read_seq(self, string):
        self.seq = [int(i) for i in string.split()]

    def lis(self, start):
        if self.cache.get(start, False):
            return self.cache[start]

        ret = 1
        for i in range(start+1, len(self.seq)):
            if start == -1 or self.seq[i] > self.seq[start]:
                ans = 1 + self.lis(i)
                if ret <= ans:
                    ret = ans
                    self.add_choice(start, i)

        self.cache[start] = ret
        return ret

    def add_choice(self, start, i):
        if start not in self.choices.keys():
            self.choices[start] = []

        self.choices[start].append(i)

    def solve(self, K):
        lis_length = self.lis(-1)-1
        print(lis_length)

        self.K = K
        self.k = 0
        return self.reconstruct_(-1, [])

    def reconstruct_(self, start, seq):
        if len(seq) == self.cache[-1]-1:
            self.k += 1
            if self.k == self.K:
                print(" ".join([str(i) for i in seq]))
            return

        for choice in sorted(self.choices[start], key=self.compare):
            seq.append(self.seq[choice])
            self.reconstruct_(choice, seq)
            seq.pop()

    def compare(self, key):
        return self.seq[key]


def main():
    C = int(input())
    for _ in range(C):
        N, K = [int(i) for i in input().split()]
        klis = KLIS()
        klis.read_seq(input())
        klis.solve(K)


if __name__ == '__main__':
    main()
