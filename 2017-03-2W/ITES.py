class ITES:
    def __init__(self, N):
        self.A = list()
        self.A.append(1983)
        i = 1
        A_i = 1983
        while i < N:
            A_i = (A_i*214013 + 2531011 ) % 2**32
            self.A.append(A_i % 10000 + 1)
            i = i + 1

    def find_seq(self, K, seq=None):
        seq = seq or self.A
        answers = set()
        partial_seq = list()
        partial_sum = 0

        while seq:
            print("!seq: ", seq)
            while partial_sum < K and seq:
                partial_sum += seq[0]
                partial_seq.append(seq.pop(0))
                print("sum: ", partial_sum)
                print("seq: ", partial_seq)

            while partial_sum > K:
                partial_sum -= partial_seq.pop(0)
                print("sum: ", partial_sum)
                print("seq: ", partial_seq)

            if partial_sum == K:
                answers.add(tuple(partial_seq))
                print("answers: ", answers)

                partial_sum -= partial_seq[0]
                partial_seq.pop(0)

        return answers
