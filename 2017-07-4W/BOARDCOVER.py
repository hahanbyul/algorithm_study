# import pprint as pp
# import colorful

class Boardcover:
    def __init__(self):
        self.board = []
        self.cache = {}

    def read_line(self, string):
        line = []
        for char in string:
            if char == '#':
                line.append(1)
            elif char == '.':
                line.append(0)

        self.board.append(line)

    def is_solvable(self, board):
        return board is not None and len(board) >= 2 and len(board[0]) >= 2 and  self.count_zero(board) % 3 == 0

    @staticmethod
    def count_zero(board):
        return sum(sum([[1 if e == 0 else 0 for e in row] for row in board], []))

    @staticmethod
    def is_full_row(board, index):
        return all(board[index])

    @staticmethod
    def is_full_col(board, index):
        return all([row[index] for row in board])

    @staticmethod
    def is_full(board):
        return all([all(row) for row in board])

    @staticmethod
    def print_board(board):
        if board is None:
            return

        for row in board:
            for char in row:
                if char == 0:
                    print(colorful.red('#'), end='')
                elif char == 2:
                    print(colorful.yellow('#'), end='')
                else:
                    print(colorful.white('#'), end='')
            print()

    @staticmethod
    def to_string(board):
        return '\n'.join([''.join(['#' if e > 0 else '.' for e in row]) for row in board])

    @staticmethod
    def to_board(string):
        board = []
        for row in string.split('\n'):
            board.append([1 if char == '#' else 0 for char in row])

        return board

    def cut_board(self, board):
        if len(board) == 0:
            return []

        if self.is_full_row(board, 0):
            return self.cut_board(board[1:])
        elif self.is_full_row(board, -1):
            return self.cut_board(board[:-1])
        elif self.is_full_col(board, 0):
            return self.cut_board([row[1:] for row in board])
        elif self.is_full_col(board, -1):
            return self.cut_board([row[:-1] for row in board])

        return board

    def fill_board(self, board, shape):
        # print(f'[FILL - {shape}]')
        for r, row in enumerate(board[:-1]):
            if all(board[r]):
                continue

            zero_index = row.index(0)
            next_row = board[r+1]

            board_ = [[e for e in row] for row in board]
            if zero_index+1 < len(row):
                if shape == 'L' and next_row[zero_index] == 0 and next_row[zero_index+1] == 0:
                    board_[r][zero_index]     = 2
                    board_[r+1][zero_index+1] = 2
                    board_[r+1][zero_index]   = 2
                    return board_

                if shape == 'L_90' and row[zero_index+1] == 0 and next_row[zero_index] == 0:
                    board_[r][zero_index]   = 2
                    board_[r][zero_index+1] = 2
                    board_[r+1][zero_index] = 2
                    return board_

                if shape == 'L_180' and row[zero_index+1] == 0 and next_row[zero_index+1] == 0:
                    board_[r][zero_index]     = 2
                    board_[r][zero_index+1]   = 2
                    board_[r+1][zero_index+1] = 2
                    return board_

            if zero_index > 0:
                if shape == 'L_270' and next_row[zero_index-1] == 0 and next_row[zero_index] == 0:
                    board_[r][zero_index]     = 2
                    board_[r+1][zero_index-1] = 2
                    board_[r+1][zero_index]   = 2
                    return board_

            return

    def solve(self, board):
        if not self.is_solvable(board):
            return 0

        """
        print('\n[SOLVE]')
        self.print_board(board)
        """

        board = self.cut_board(board)

        """
        print('\n[CUT]')
        self.print_board(board)
        print()
        """

        if board == []:
            return 1

        if not self.is_solvable(board):
            return 0

        # memoization check
        board_str = self.to_string(board)
        if self.cache.get(board_str, False):
            # print('\n[CACHED]')
            return self.cache[board_str]

        # split board
        for r in range(1, len(board)-1):
            if self.is_full_row(board, r):
                # print('\n[SPLIT]')
                return self.solve(board[:r]) * self.solve(board[r+1:])

        for c in range(1, len(board[0])-1):
            if self.is_full_col(board, c):
                # print('\n[SPLIT]')
                return self.solve([row[:c] for row in board]) * self.solve([row[c+1:] for row in board])

        ret = self.solve(self.fill_board(board, 'L')) + self.solve(self.fill_board(board, 'L_90')) + self.solve(self.fill_board(board, 'L_180')) + self.solve(self.fill_board(board, 'L_270'))
        self.cache[self.to_string(board)] = ret
        return ret

    """
    def print_cache(self):
        for key, val in self.cache.items():
            print(f'key: -> val: {val}')
            self.print_board(self.to_board(key))
    """


def main():
    C = int(input())
    for _ in range(C):
        bc = Boardcover()

        H, W = [int(i) for i in input().split()]
        for _ in range(H):
            bc.read_line(input())

        print(bc.solve(bc.board))

if __name__ == '__main__':
    main()

