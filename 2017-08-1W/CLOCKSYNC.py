# https://algospot.com/judge/problem/read/CLOCKSYNC
import numpy as np

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

        self.switch_mat = self.get_switch_mat()
        self.identity_mat = self.get_identity_mat()
        self.pivotted = {}

    def get_switch_mat(self):
        mat = []
        for indices in self.switch.values():
            mat.append([-1 if i in indices else 0 for i in range(16)])

        return mat

    def get_identity_mat(self):
        return [[0 if i != j else 1 for j in range(16)] for i in range(16)]

    def bfs(self, problem):
        visited = {}
        queue = []
        queue.append((problem, 0))

        while len(queue) > 0:
            cur_state, distance = queue.pop(0)
            # print(f'state: {cur_state}, dist: {distance}')
            if cur_state == tuple([12] * 16):
                return distance

            # print(f'next: {self.get_next(cur_state)}')
            for next_state in self.get_next(cur_state):
                if not visited.get(next_state, False):
                    queue.append((next_state, distance + 1))
                    visited[next_state] = True
            # print(f'q: {queue}')

    def get_next(self, cur_state):
        next_state_list = []
        for switch_num, indices in enumerate(self.switch.values()):
            # if any([cur_state[i] != 12 for i in indices]):
            next_state = self.push_switch(cur_state, switch_num)
            next_state_list.append(next_state)

        return next_state_list

    def push_switch(self, cur_state, switch_num):
        next_state = list(cur_state)
        for i in self.switch[switch_num]:
            next_state[i] -= 3
            if next_state[i] == 0:
                next_state[i] = 12

        return tuple(next_state)

    @staticmethod
    def add_multiple_row(mat, i, j, scaler):
        print(f'i: {i}, j: {j}, scaler: {scaler}')
        mat[j] = [e_j + scaler * e_i for e_i, e_j in zip(mat[i], mat[j])]
        return mat
    
    @staticmethod
    def swap_rows(mat, i, j):
        print(f'mat[i]: {mat[i]}, mat[j]: {mat[j]}')
        mat[i], mat[j] = mat[j], mat[i]
        return mat

    def pivotting(self, mat, j):
        self.print_matrix(mat)
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
                self.add_multiple_row(mat, pivot, i, int(-mat[i][j]/mat[pivot][j]))
                self.add_multiple_row(self.identity_mat, pivot, i, int(-mat[i][j]/mat[pivot][j]))

            i += 1

        self.swap_rows(mat, pivot, j)
        self.swap_rows(self.identity_mat, pivot, j)
        self.print_matrix(mat)
        self.print_matrix(self.identity_mat)

    @staticmethod
    def print_matrix(mat):
        print(f'mat: \n{np.array(mat)}')

