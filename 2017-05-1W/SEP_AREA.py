# https://www.acmicpc.net/problem/2583


class Separated_area:
    def __init__(self):
        self.dx = [1,0,-1,0]
        self.dy = [0,1,0,-1]

    def read_problem(self, string):
        self.M, self.N, self.K = [int(i) for i in string.split()]
        self.board = [[False for _ in range(self.N)] for _ in range(self.M)]

    def read_rect(self, string):
        points = [int(i) for i in string.split()]
        self.fill_rect(points)

    def fill_rect(self, points):
        for i in range(points[1], points[3]):
            for j in range(points[0], points[2]):
                self.board[i][j] = True

    def dfs_stack(self, i, j):
        stack = list()
        stack.append((i,j))
        self.board[i][j] = True
        ret = 0

        while len(stack) > 0:
            x, y = stack.pop()
            ret += 1
            for dx, dy in zip(self.dx, self.dy): 
                x_next = x + dx
                y_next = y + dy

                inside = 0 <= x_next < self.M and 0 <= y_next < self.N
                if inside and not self.board[x_next][y_next]:
                    stack.append((x_next, y_next))
                    self.board[x_next][y_next] = True

        return ret

    def solve(self):
        areas = list()
        for i in range(self.M):
            for j in range(self.N):
                if self.board[i][j]:
                    continue
                areas.append(self.dfs_stack(i,j))

        print(len(areas))
        print(" ".join([str(i) for i in sorted(areas)]))


def main():
    problem = Separated_area()
    prob = input()
    problem.read_problem(prob)

    for _ in range(problem.K):
        rect = input()
        problem.read_rect(rect) 

    problem.solve()

if __name__ == '__main__':
    main()
