from pprint import pprint

class CoinOnTheTable:
    def __init__(self):
        self.dist = {}
        self.path_coord = {}
        self.path_coord[''] = (0,0)
        self.cache = {}

    def read_numbers(self, string):
        self.N, self.M, self.K = [int(x) for x in string.split()]

    def read_board(self, string):
        self.board = [[0 for _ in range(self.M)] for _ in range(self.N)]
        for i, row in enumerate(string.split('\n')):
            for j in range(self.M):
                self.board[i][j] = row[j]
        self.board_init = [[x for x in row] for row in self.board]

    def find_star(self):
        for i in range(self.N):
            try:
                j = self.board_init[i].index('*')
            except ValueError:
                continue

        return (i, j)

    def min_dist(self):
        return sum(self.find_star())


    def find_path(self, board):
        board_str = self.board_to_string(board)
        ret = self.cache.get(board_str, False)
        if ret:
            return ret

        i, j = 0, 0
        visited = {}

        path = ''
        current = self.board[i][j]
        while current != '*':
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

            if i < 0 or i >= self.N or j < 0 or j >= self.M:
                self.cache[board_str] = (False, path)
                return self.cache[board_str]
            if visited.get((i,j), False):
                self.cache[board_str] = (False, path)
                return self.cache[board_str]

            current = self.board[i][j]

        self.cache[board_str] = (True, path)
        return self.cache[board_str]

    @staticmethod
    def board_to_string(board):
        return ''.join([''.join([x for x in row]) for row in board])

    @staticmethod
    def string_to_board(string, N, M):
        return [[string[i*M + j] for j in range(M)] for i in range(N)]

    def print_board(self, board):
        for row in board:
            print(''.join(row))
        print('-'*self.M)

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

    def edit_board(self, change):
        for (i, j) in change.keys():
            self.board[i][j] = change[(i,j)]
        return self.board

    def recover_board(self, change):
        for (i, j) in change.keys():
            self.board[i][j] = self.board_init[i][j]
        return self.board

    def solve(self):
        k = 0
        changes = [{}]

        min_val = self.min_dist()
        if min_val > self.K:
            print(-1)
            return

        while k <= min_val:
            changes = self.is_possible_in_K(changes)
            if len(changes) == 0:
                break
            k += 1

        print(k)
        # print('N: %d, M: %d, K: %d' % (self.N, self.M, self.K))
        # self.print_board(self.board_init)
        return k

    def is_possible_in_K(self, changes):
        next_changes = []

        for change in changes:
            # print(change)
            board = self.edit_board(change)
            success, path = self.find_path(board)

            # self.print_board(board)
            # print('path: %s' % path)

            if success and len(path) <= self.K:
                self.answer_board = self.board
                self.answer_path  = path
                self.answer_change = change
                return []

            self.recover_board(change)
            next_changes += self.get_next_change(change)

        return next_changes

    def get_next_change(self, change):
        next_change = []
        _, path = self.find_path(self.edit_board(change))
        self.recover_board(change)

        for i in range(len(path)):
            coord = self.find_path_coord(path[:i+1])
            if coord not in change.keys():
                x, y = coord
                for ch in ['L', 'R', 'U', 'D']:
                    if self.board_init[x][y] == ch:
                        continue
                    new_change = change.copy()
                    new_change[(x,y)] = ch
                    next_change.append(new_change)

        return next_change


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
