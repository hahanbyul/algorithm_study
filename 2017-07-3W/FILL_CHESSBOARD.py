# https://www.acmicpc.net/problem/1018

class Board:
    def __init__(self, height):
        self.board = []
        self.height = height

    def read_board(self, string):
        self.board.append(list(string))

    def sum_total_fill(self, array):
        ret = 0
        for i, s in enumerate(array):
            if i % 2 == 0:
                ret += s
            else:
                ret += self.height - s

        return min(ret, self.height * self.height - ret)

    def how_many_fill(self, array):
        ret = 0
        for i, e in enumerate(array):
            if i % 2 == 0 and e != 'W':
                ret += 1
            if i % 2 == 1 and e != 'B':
                ret += 1

        return ret

    def compute_next(self, current, old, new):
        next_array = [self.height - s for s in current]
        for i in range(self.height):
            if old[i] == 'W':
                next_array[i] -= 1

            if new[i] == 'W':
                next_array[i] += 1

        return next_array

    def get_row(self, row_begin, col_begin):
        return self.board[row_begin][col_begin:col_begin + self.height]

    def get_col(self, row_begin, col_begin):
        return [self.board[r][col_begin] for r in range(row_begin, row_begin + self.height)]

    def solve(self):
        prev_array = [self.how_many_fill(self.get_row(i, 0)) for i in range(self.height)]
        # print(f'init: {prev_array}')
        min_fill = self.sum_total_fill(prev_array)
        next_array = prev_array

        for r in range(len(self.board) - self.height + 1):
            # print(f'row: {r}')
            for c in range(len(self.board[0]) - self.height):
                next_array = self.compute_next(next_array, self.get_col(r, c), self.get_col(r, c + self.height))
                min_fill = min(min_fill, self.sum_total_fill(next_array))
                """
                print(f'col: {c}')
                print(f'old: {self.get_col(r,c)}, new: {self.get_col(r, c + self.height)}')
                print(f'next: {next_array}')
                print(f'sum_total: {self.sum_total_fill(next_array)}')
                print(f'min: {min_fill}')
                """

            if r == len(self.board) - self.height:
                break

            prev_array.pop(0)
            prev_array.append(self.how_many_fill(self.get_row(r + self.height, 0)))
            next_array = prev_array
            min_fill = min(min_fill, self.sum_total_fill(next_array))

            if min_fill == 0:
                return 0

            """
            print(f'init: {prev_array}')
            print(f'sum_total: {self.sum_total_fill(next_array)}')
            print(f'min: {min_fill}')
            """
        return min_fill


def main():
    M, N = [int(i) for i in input().split()]
    board = Board(8)

    for _ in range(M):
        board.read_board(input())

    print(board.solve())

if __name__ == '__main__':
    main()
