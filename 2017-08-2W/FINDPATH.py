class Findpath:
    def __init__(self, N):
        self.graph = []
        self.N = N

    def read_graph(self):
        for _ in range(self.N):
            self.read_line(input())

    def read_line(self, string):
        self.graph.append([int(i) for i in string.split()])

    def get_reachable(self):
        return [[e if e == 1 else float('inf') for e in row] for row in self.graph]

    def floyd(self):
        reachable = self.get_reachable()

        for k in range(self.N):
            for i in range(self.N):
                for j in range(self.N):
                    if reachable[i][j] > reachable[i][k] + reachable[k][j]:
                        reachable[i][j] = reachable[i][k] + reachable[k][j]

        return reachable

    def solve(self):
        ret = self.reformat(self.floyd())
        self.print_mat(ret)
        return ret

    def reformat(self, array):
        return [[0 if e == float('inf') else 1 for e in row] for row in array]

    def print_mat(self, array):
        for row in array:
            print(' '.join([str(i) for i in row]))


def main():
    N = int(input())
    fp = Findpath(N)
    fp.read_graph()
    fp.solve()

if __name__ == '__main__':
    main()
