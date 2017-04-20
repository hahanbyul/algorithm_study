import numpy as np

class Numb3rs:
    def __init__(self, N, D, P):
        self.N = N
        self.D = D
        self.P = P

        self.day_0 = [0.0 for _ in range(self.N)]
        self.day_0[P] = 1.0

    def read_table(self):
        self.trans = list()
        for _ in range(self.N):
            trans = [float(i) for i in input().split()]
            self.trans.append(trans)
        self.trans = np.array(self.trans)
        for i in range(self.N):
            self.trans[i,:] /= float(np.sum(self.trans[i,:]))

    def read_table_as_string(self, string):
        self.trans = list()
        table_str = string.split('\n')
        for row in table_str:
            trans = [float(i) for i in row.split()]
            self.trans.append(trans)
        self.trans = np.array(self.trans)
        for i in range(self.N):
            self.trans[i,:] /= float(np.sum(self.trans[i,:]))

    def get_answer(self, Q):
        answer = np.dot(self.day_0, np.linalg.matrix_power(self.trans, self.D))
        return answer[Q]

def main():
    C = int(input())
    for _ in range(C):
        N, D, P = [int(i) for i in input().split()]
        number = Numb3rs(N, D, P)
        number.read_table()
        T = input()
        Q = [int(i) for i in input().split()]
        answer = [str(num) for num in number.get_answer(Q).tolist()]
        print(" ".join(answer))

if __name__ == '__main__':
    main()
