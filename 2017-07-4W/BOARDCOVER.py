import pprint as pp
import colorful

class Boardcover:
    def __init__(self):
        self.board = []

    def read_board(self, H, W):
        self.board = [[1 for _ in range(W)] for _ in range(H)]
        for h in range(H):
            line = input()
            for w, char in enumerate(line):
                if char == '.':
                    self.board[h][w] = 0

        print(self.board)

    def read_line(self, string):
        self.board.append([1 if char == '#' else 0 for char in string])

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
        print(f'[FILL - {shape}]')
        for r, row in enumerate(board[:-1]):
            if all(board[r]):
                continue

            zero_index = row.index(0)
            next_row = board[r+1]

            board_ = [[e for e in row] for row in board]
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

            if shape == 'L_270' and zero_index > 0 and next_row[zero_index-1] == 0 and next_row[zero_index] == 0:
                board_[r][zero_index]     = 2
                board_[r+1][zero_index-1] = 2
                board_[r+1][zero_index]   = 2
                return board_

            return

    def solve(self, board):
        print('\n[SOLVE]')
        self.print_board(board)

        board = self.cut_board(board)

        print('\n[CUT]')
        self.print_board(board)
        print()

        if board == []:
            return 1

        # memoization check

        # split board
        for r in range(1, len(board)-1):
            if self.is_full_row(board, r):
                print('\n[SPLIT]')
                return self.solve(board[:r]) * self.solve(board[r+1:])

        for c in range(1, len(board[0])-1):
            if self.is_full_col(board, c):
                return self.solve([row[:c] for row in board]) * self.solve([row[c+1:] for row in board])

        # return self.fill(board)
        self.print_board(self.fill_board(board, 'L'))
        self.print_board(self.fill_board(board, 'L_90'))
        self.print_board(self.fill_board(board, 'L_180'))
        self.print_board(self.fill_board(board, 'L_270'))

    def split_board(self, row_begin, row_end, col_begin, col_end):
        print('%d, %d, %d, %d' % (row_begin, row_end, col_begin, col_end))

        for r in range(row_begin+1, row_end-1):
            if self.is_full_row(r):
                return self.split_board(row_begin, r, col_begin, col_end) * self.split_board(r+1, row_end, col_begin, col_end)

        for c in range(col_begin+1, col_end-1):
            if self.is_full_col(c):
                return self.split_board(row_begin, row_end, col_begin, c) * self.split_board(row_begin, row_end, c+1, col_end)

        ret = self.solve([[self.board[r][c] for c in range(col_begin, col_end)] for r in range(row_begin, row_end)])
        print(f'way = {ret}')
        return ret
            
    def fill(self, subboard):
        print('\n[FILL]')
        if all([all(row) for row in subboard]):
            return 1

        ret = 0
        for r, row in enumerate(subboard[:-1]):
            if all(subboard[r]):
                continue

            next_row = subboard[r+1]
            zero_index = row.index(0)
            if zero_index > 0 and next_row[zero_index-1] == 0 and next_row[zero_index] == 0:
                subboard_copy = subboard.copy()
                subboard_copy[r][zero_index]     = 1
                subboard_copy[r+1][zero_index-1] = 1
                subboard_copy[r+1][zero_index]   = 1
                ret += self.solve(subboard_copy)

            if next_row[zero_index+1] == 0 and next_row[zero_index] == 0:
                subboard_copy = subboard.copy()
                subboard_copy[r][zero_index]     = 1
                subboard_copy[r+1][zero_index+1] = 1
                subboard_copy[r+1][zero_index]   = 1
                ret += self.solve(subboard_copy)

            if row[zero_index+1] == 0 and next_row[zero_index] == 0:
                subboard_copy = subboard.copy()
                subboard_copy[r][zero_index]   = 1
                subboard_copy[r][zero_index+1] = 1
                subboard_copy[r+1][zero_index] = 1
                ret += self.solve(subboard_copy)

            if row[zero_index+1] == 0 and next_row[zero_index+1] == 0:
                subboard_copy = subboard.copy()
                subboard_copy[r][zero_index]     = 1
                subboard_copy[r][zero_index+1]   = 1
                subboard_copy[r+1][zero_index+1] = 1
                ret += self.solve(subboard_copy)

        print(ret)
        return ret
