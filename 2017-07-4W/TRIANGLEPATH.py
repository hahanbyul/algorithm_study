class Trianglepath:
    def __init__(self):
        self.triangle = []
        self.cache = {}

    def read_line(self, string):
        self.triangle.append([int(i) for i in string.split()])

    def solve(self, n):
        for i in range(n):
            self.max_path(n-1, i)
        ret = max([self.cache[(n-1, i)] for i in range(n)])
        print(ret)
        return ret

    def max_path(self, i, j):
        if self.cache.get((i,j), False):
            return self.cache[(i,j)]

        if i == 0:
            ret = self.triangle[0][0]
        elif j == 0:
            ret = self.triangle[i][0] + self.max_path(i-1, 0)
        elif i == j:
            ret = self.triangle[i][j] + self.max_path(i-1, j-1)
        else:
            ret = self.triangle[i][j] + max(self.max_path(i-1, j), self.max_path(i-1, j-1))

        self.cache[(i,j)] = ret
        return ret


def main():
    C = int(input())
    for _ in range(C):
        tri = Trianglepath()
        n = int(input())
        for _ in range(n):
            tri.read_line(input())

        tri.solve(n)


if __name__ == '__main__':
    main()
