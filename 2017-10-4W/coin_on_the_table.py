class CoinOnTheTable:
    def __init__(self):
        self.dist = {}
        self.path_coord = {}
        self.path_coord[''] = (0,0)

    def read_numbers(self, string):
        self.N, self.M, self.K = [int(x) for x in string.split()]

    def read_board(self, string):
        self.board = [[0 for _ in range(self.M)] for _ in range(self.N)]
        for i, row in enumerate(string.split('\n')):
            for j in range(self.M):
                self.board[i][j] = row[j]

    def find_star(self):
        for i in range(self.N):
            try:
                j = self.board[i].index('*')
            except ValueError:
                continue

        return (i, j)

    def min_dist(self):
        return sum(self.find_star())

    def solve(self):
        if self.min_dist() > self.K:
            print(-1)
            return

    def find_path(self, board):
        # caching!
        i, j = 0, 0
        visited = {}

        path = ''
        current = self.board[i][j]
        while current != '*':
            if i < 0 or i >= self.N or j < 0 or j >= self.M:
                return float('inf')
            if visited.get((i,j), False):
                return float('inf')

            path += current
            visited[(i,j)] = True

            if current == 'U':
                i -= 1
            elif current == 'D':
                i += 1
            elif current == 'L':
                j -= 1
            elif current == 'R':
                j += 1
            current = self.board[i][j]

        return path

    @staticmethod
    def board_to_string(board):
        return ''.join([''.join([x for x in row]) for row in board])

    @staticmethod
    def string_to_board(string, N, M):
        return [[string[i*M + j] for j in range(M)] for i in range(N)]

    def change_board(board, index):
        path = self.find_path(board)

    def find_path_coord(self, path):
        coord = self.path_coord[path[:-1]]
        last = path[-1]

        i, j = coord
        if last == 'U':
            i -= 1
        elif last == 'D':
            i += 1
        elif last == 'L':
            j -= 1
        elif last == 'R':
            j += 1
        self.path_coord[path] = (i, j)

        return coord

    def solve(self):
        next_board = change_board(board, index)
        next_path = self.find_path(next_board)
        self.dist[next_path] = self.dist[path] + 1

