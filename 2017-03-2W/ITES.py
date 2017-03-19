class ITES:
    def __init__(self, N):
        self.N = N
        self.seq = self.generator(N)

    def generator(self, N=None):
        N = N or self.N
        yield 1983
        i = 1
        A_i = 1983
        while i < N:
            A_i = (A_i*214013 + 2531011 ) % 2**32
            yield A_i % 10000 + 1
            i += 1

    def find_seq(self, K, seq=None):
        seq = seq or self.seq
        answers = set()
        partial_seq = list()
        partial_sum = 0

        try:
            while True:
                while partial_sum < K:
                    #x = seq.__next__()
                    x = next(seq)
                    partial_sum += x
                    partial_seq.append(x)
                    #print("sum: ", partial_sum)
                    #print("seq: ", partial_seq)

                while partial_sum > K:
                    partial_sum -= partial_seq.pop(0)

                if partial_sum == K:
                    answers.add(tuple(partial_seq))

                    partial_sum -= partial_seq[0]
                    partial_seq.pop(0)

        except StopIteration:
            return answers

def main():
    C = int(input())
    for _ in range(C):
        #K, N = tuple([int(i) for i in input().split()])
        K, N = tuple([int(i) for i in raw_input().split()])
        ites = ITES(N)
        print(len(ites.find_seq(K)))
    """
    K, N = (3578452, 5000000)
    ites = ITES(N)
    print(len(ites.find_seq(K)))
    """

if __name__ == '__main__':
    main()
