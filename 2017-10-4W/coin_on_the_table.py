class CoinOnTheTable:
    def __init__(self):
        pass

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
        i, j = 0, 0
        path = ''

        current = self.board[i][j]
        while current != '*':
            if i < 0 or i >= self.N or j < 0 or j >= self.M:
                return ''

            path += current

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

