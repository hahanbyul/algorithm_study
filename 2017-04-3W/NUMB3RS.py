# https://algospot.com/judge/problem/read/NUMB3RS
import math

class Numb3rs:
    def __init__(self, N, D, P):
        self.N = N
        self.D = D
        self.P = P

        self.day_0 = [0.0 for _ in range(self.N)]
        self.day_0[P] = 1.0

        self.cache = dict()

    def read_table(self):
        self.trans = list()
        for _ in range(self.N):
            trans = [float(i) for i in input().split()]
            self.trans.append(trans)
        self.normalize()

    def normalize(self):
        for i in range(self.N):
            row_sum = float(sum(self.trans[i]))
            for j in range(self.N):
                self.trans[i][j] /= row_sum

    def read_table_as_string(self, string):
        self.trans = list()
        table_str = string.split('\n')
        for row in table_str:
            trans = [float(i) for i in row.split()]
            self.trans.append(trans)
        self.normalize()

    def get_answer(self, Q):
        answer = self.vec_matmul(self.day_0, self.matpower(self.trans, self.D))
        answer_in_Q = list()
        for q in Q:
            answer_in_Q.append(answer[q])

        return answer_in_Q

    def vec_matmul(self, X, Y):
        J = len(Y[0])
        K = len(Y)
        XY = [0.0 for _ in range(J)]

        for j in range(J):
           for k in range(K):
               XY[j] += X[k] * Y[k][j]

        return XY

    def matmul(self, X, Y):
        I = len(X)
        J = len(Y[0])
        K = len(Y)
        XY = [[0.0 for _ in range(J)] for _ in range(I)]

        for i in range(I):
            for j in range(J):
               for k in range(K):
                   XY[i][j] += X[i][k] * Y[k][j]

        return XY

    def matpower(self, X, power):
        if self.cache.get(power, False):
            return self.cache[power]
        if power == 1:
            return X

        if power % 2 == 0:
            ret = self.matmul(self.matpower(X, power/2), self.matpower(X, power/2))
        else:
            split_num = math.ceil(power/2)
            ret = self.matmul(self.matpower(X, split_num), self.matpower(X, power - split_num))

        self.cache[power] = ret
        return ret


def main():
    C = int(input())
    for _ in range(C):
        N, D, P = [int(i) for i in input().split()]
        number = Numb3rs(N, D, P)
        number.read_table()
        T = input()
        Q = [int(i) for i in input().split()]
        answer = [str(num) for num in number.get_answer(Q)]
        print(" ".join(answer))

if __name__ == '__main__':
    main()
