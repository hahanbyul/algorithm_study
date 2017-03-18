class ITES:
    def __init__(self, K):
        self.A = list()
        self.A.append(1983)
        i = 1
        A_i = 1983
        while i < K:
            A_i = (A_i*214013 + 2531011 ) % 2**32
            self.A.append(A_i % 10000 + 1)
            i = i + 1
