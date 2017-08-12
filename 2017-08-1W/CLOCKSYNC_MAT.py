# https://algospot.com/judge/problem/read/CLOCKSYNC

class Clocksync:
    def __init__(self):
        self.switch = {0: (0, 1, 2), \
                1: (3, 7, 9, 11), \
                2: (4, 10, 14, 15), \
                3: (0, 4, 5, 6, 7), \
                4: (6, 7, 8, 10, 12), \
                5: (0, 2, 14, 15), \
                6: (3, 14, 15), \
                7: (4, 5, 7, 14, 15), \
                8: (1, 2, 3, 4, 5), \
                9: (3, 4, 5, 9, 13)}

        self.answer = tuple([12] * 16)
        self.switch_mat   = self.get_switch_mat()
        self.identity_mat = self.get_identity_mat()

        for i in range(10):
            self.pivotting(self.switch_mat, i)

    def get_switch_mat(self):
        mat = [[0 for _ in range(10)] for _ in range(16)]
        for col in range(10):
            for row in self.switch[col]:
                mat[row][col] = 1

        return mat

    def get_identity_mat(self):
        return [[0 if i != j else 1 for j in range(16)] for i in range(16)]

    def get_state_mat(self, string):
        return self.modularize([int(num) // 3 for num in string.split()])

    def modularize(self, array):
        return [num % 4 for num in array]

    @staticmethod
    def add_multiple_row(mat, i, j, scaler):
        # print(f'i: {i}, j: {j}, scaler: {scaler}')
        mat[j] = [e_j + scaler * e_i for e_i, e_j in zip(mat[i], mat[j])]
        return mat
    
    @staticmethod
    def swap_rows(mat, i, j):
        # print(f'mat[i]: {mat[i]}, mat[j]: {mat[j]}')
        mat[i], mat[j] = mat[j], mat[i]
        return mat

    def pivotting(self, mat, j):
        # self.print_matrix(mat)
        i = j
        while i < 10 and mat[i][j] == 0:
            i += 1
        if i == 10:
            return

        pivot = i

        # i += 1
        i = 0
        while i < 10:
            if i != pivot and mat[i][j] != 0:
                scaler = int(-mat[i][j]/mat[pivot][j])
                self.add_multiple_row(mat, pivot, i, scaler)
                self.add_multiple_row(self.identity_mat, pivot, i, scaler)

            i += 1

        self.swap_rows(mat, pivot, j)
        self.swap_rows(self.identity_mat, pivot, j)
        # self.print_matrix(mat)
        # self.print_matrix(self.identity_mat)

    def solve(self, string):
        LA = self.switch_mat
        L = self.identity_mat
        b = self.get_state_mat(string)

        Lb = []
        for i in range(16):
            e = sum([e_iden * (-e_prob) for e_iden, e_prob in zip(L[i], b)])
            Lb.append(e)

        x = {}
        x[0] = Lb[0] % 4
        x[1] = Lb[11] % 4
        x[2] = Lb[2] % 4
        x[3] = -Lb[3] % 4
        x[4] = Lb[4] % 4
        x[5] = -Lb[5] % 4
        x[6] = -Lb[6] % 4
        x[8] = -Lb[8] % 4
        x[9] = (Lb[9] // 2) % 4
        x[7] = (Lb[7] - x[9]) % 4
        
        if self.is_correct(x, string):
            ret = 0
            for i in range(10):
                ret += x[i]
            return ret
        else:
            return -1

    def is_correct(self, x, string):
        cur_state = tuple([int(i) for i in string.split()])
        for i in range(10):
            for _ in range(x[i]):
                cur_state = self.push_switch(cur_state, i)

        return cur_state == self.answer

    def push_switch(self, cur_state, switch_num):
        next_state = list(cur_state)
        for i in self.switch[switch_num]:
            next_state[i] += 3
            if next_state[i] == 15:
                next_state[i] = 3

        return tuple(next_state)

def main():
    C = int(input())
    for _ in range(C):
        cs = Clocksync()
        print(cs.solve(input()))

if __name__ == '__main__':
    main()
