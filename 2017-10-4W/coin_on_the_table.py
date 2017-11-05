from pprint import pprint

class CoinOnTheTable:
    def __init__(self):
        self.direction = {}
        self.direction[(-1, 0)] = 'D'
        self.direction[(1, 0)]  = 'U'
        self.direction[(0, -1)] = 'R'
        self.direction[(0, 1)]  = 'L'

    def read_numbers(self, string):
        self.N, self.M, self.K = [int(x) for x in string.split()]
        self.cache = [[[float('inf') for _ in range(self.M)] for _ in range(self.N)] for _ in range(self.K+1)]

    def read_board(self, string):
        self.board = [[0 for _ in range(self.M)] for _ in range(self.N)]
        for i, row in enumerate(string.split('\n')):
            for j in range(self.M):
                self.board[i][j] = row[j]
        self.board_init = [[x for x in row] for row in self.board]

    def print_board(self, board):
        for row in board:
            print(''.join(row))
        print('-'*self.M)

    def print_cache(self, t):
        print('t = %d' % t)
        for row in self.cache[t]:
            print(row)

    def solve(self):
        self.cache[0][0][0] = 0
        # self.print_cache(0)

        ret = float('inf')

        for t in range(1, self.K+1):
            for i in range(self.N):
                for j in range(self.M):
                    if i + j > self.K:
                        continue

                    self.cache[t][i][j] = self.check_neighbor(t, i, j)

                    if self.board[i][j] == '*':
                        ret = min(ret, self.cache[t][i][j])

            # self.print_cache(t)

        if ret == float('inf'):
            print(-1)
        else:
            print(ret)
        return ret

    def check_neighbor(self, t, i, j):
        ret = float('inf')

        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            if not self.is_in_board(i+di, j+dj):
                continue

            cand = self.cache[t-1][i+di][j+dj]
            if self.board[i+di][j+dj] != self.direction[(di,dj)]:
                cand += 1

            ret = min(ret, cand)

        return ret

    def is_in_board(self, i, j):
        if 0 <= i < self.N and 0 <= j < self.M:
            return True
        else:
            return False

def main():
    cot = CoinOnTheTable()
    cot.read_numbers(input())

    board = []
    for n in range(cot.N):
        board.append(input())
    board_str = '\n'.join(board)
    cot.read_board(board_str)

    cot.solve()


if __name__ == '__main__':
    main()
