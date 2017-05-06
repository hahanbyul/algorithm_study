# https://www.acmicpc.net/problem/2583
import sys
sys.setrecursionlimit(10000)


class Separated_area:
    def __init__(self):
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]

    def read_problem(self, string):
        self.M, self.N, self.K = [int(i) for i in string.split()]
        self.board = [[0 for _ in range(self.N)] for _ in range(self.M)]

    def read_rect(self, string):
        points = [int(i) for i in string.split()]
        self.fill_rect(points)

    def fill_rect(self, points):
        for i in range(points[1], points[3]):
            for j in range(points[0], points[2]):
                self.board[i][j] = 1

    def dfs(self, i, j):
        # print(f'dfs({i},{j})')
        self.board[i][j] = 2 # visited
        ret = 1

        for di, dj in zip(self.dx, self.dy): 
            i_next = i + di
            j_next = j + dj
            if i_next < 0 or j_next < 0 or i_next >= self.M or j_next >= self.N:
                continue
            if self.board[i_next][j_next] > 0:
                continue
            ret += self.dfs(i_next, j_next)

        return ret

    def solve(self):
        cnt = 0
        areas = list()
        for i in range(self.M):
            for j in range(self.N):
                if self.board[i][j] > 0:
                    continue
                cnt += 1
                areas.append(self.dfs(i,j))

        print cnt
        print " ".join([str(i) for i in sorted(areas)])


def main():
    problem = Separated_area()
    prob = raw_input()
    problem.read_problem(prob)

    for _ in range(problem.K):
        rect = raw_input()
        problem.read_rect(rect) 

    # pp.pprint(problem.board)
    problem.solve()

if __name__ == '__main__':
    main()
