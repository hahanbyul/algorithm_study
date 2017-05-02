# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1113&sca=30
import pprint as pp
import colorful


class Cheese:
    def __init__(self, board):
        if isinstance(board, str):
            board = self.parse_board(board)

        self.board = board

        self.is_row_empty = [False for _ in range(len(board))]
        self.is_col_empty = [False for _ in range(len(board[0]))]

        self.is_row_empty[0] = True
        self.is_row_empty[-1] = True
        self.is_col_empty[0] = True
        self.is_col_empty[-1] = True

        self.row_first = dict()
        self.col_first = dict()
        self.row_last  = dict()
        self.col_last  = dict()

        self.row_hole = dict()
        self.col_hole = dict()

        self.opened_holes = list()

    def parse_board(self, board_str):
        return [[int(i) for i in row_str.split()]for row_str in board_str.split('\n')]

    def get_melting_cheese(self, line):
        cheese = self.cheese_idx(line)
        return [cheese[0], cheese[-1]]
            
    def first_cheese(self, line, begin):
        for i in range(begin+1, len(line)):
            if line[i-1] == 0 and line[i] == 1:
                break
        return i
            
    def last_cheese(self, line, begin):
        i = self.first_cheese(line[::-1], len(line)-1-begin)
        return len(line)-1-i
            
    def row(self, i):
        return self.board[i]
            
    def col(self, j):
        return [row[j] for row in self.board]

    def edge_iter(self, mode):
        if mode == 'row':
            is_empty = self.is_row_empty
            get_line = self.row
            first = self.row_first
            last = self.row_last
        elif mode == 'col':
            is_empty = self.is_col_empty
            get_line = self.col
            first = self.col_first
            last = self.col_last

        for i in range(len(is_empty)):
            if is_empty[i]:
                continue
                            
            line = get_line(i)
            first[i] = self.first_cheese(line, first.get(i, 0))
            last[i]  = self.last_cheese(line, last.get(i, len(line)-1))
            
            if first[i] == len(line)-1:
                is_empty[i] = True

    def get_row_edge(self, i):
        if self.is_row_empty[i]:
            return None
        else:
            return self.row_first[i], self.row_last[i]

    def get_col_edge(self, i):
        if self.is_col_empty[i]:
            return None
        else:
            return self.col_first[i], self.col_last[i]

    def hole_iter(self, mode):
        if mode == 'row':
            is_empty = self.is_row_empty
            get_line = self.row
            first = self.row_first
            last = self.row_last
            hole_list = self.row_hole
        elif mode == 'col':
            is_empty = self.is_col_empty
            get_line = self.col
            first = self.col_first
            last = self.col_last
            hole_list = self.col_hole

        for i in range(len(is_empty)):
            if is_empty[i]:
                continue
                            
            line = get_line(i)
            hole_right = self.first_cheese(line, first[i])
            found = list()
            while hole_right <= last[i]:
                hole_left = self.last_cheese(line, hole_right)
                found.append(Hole((hole_left, hole_right), mode, i))
                hole_right = self.first_cheese(line, hole_right)

            if len(found) > 0:
                hole_list[i] = found

    def get_row_hole(self, i):
        return [(hole.left, hole.right) for hole in self.row_hole.get(i, [])]

    def get_col_hole(self, i):
        return [(hole.left, hole.right) for hole in self.col_hole.get(i, [])]
                    
    def has_hole(self, i):
        return len(self.row_hole[i]) > 0
            
    def explore_row_hole(self, idx, direction):
        cur_left, cur_right = self.row_hole[idx].pop(0)
        
        next_left, next_right = next_holes[0]
        if next_left <= cur_right:
            self.explore_row_hole(self, idx + direction, direction)

    def color_row_edge(self, board=None):
        if board is None:
            board = self.board

        for i in range(len(board)):
            if self.is_row_empty[i]:
                continue

            edge = self.get_row_edge(i)
            if edge is not None:
                board[i][edge[0]] = 6
                board[i][edge[1]] = 6
        return board

    def color_row_hole(self, board=None):
        if board is None:
            board = self.board

        for i in range(len(board)):
            if self.is_row_empty[i]:
                continue

            hole = self.get_row_hole(i)
            for h in hole:
                board[i][h[0]] = 7
                board[i][h[1]] = 7

        return board

    def color_col_edge(self, board=None):
        if board is None:
            board = self.board

        for i in range(len(board[0])):
            if self.is_col_empty[i]:
                continue

            edge = self.get_col_edge(i)
            if edge is not None:
                board[edge[0]][i] = 6
                board[edge[1]][i] = 6
        return board

    def color_col_hole(self, board=None):
        if board is None:
            board = self.board

        for i in range(len(board[0])):
            if self.is_col_empty[i]:
                continue

            hole = self.get_col_hole(i)
            for h in hole:
                board[h[0]][i] = 7
                board[h[1]][i] = 7
        return board

    def color_opened_hole(self, board=None):
        if board is None:
            board = self.board

        for hole in self.opened_holes:
            self.color_hole_iter(board, hole)

        return board

    def color_hole_iter(self, board, hole):
        hole.colored = True

        if hole.mode == 'row':
            board[hole.idx][hole.left] = 6
            board[hole.idx][hole.right] = 6
        elif hole.mode == 'col':
            board[hole.left][hole.idx] = 6
            board[hole.right][hole.idx] = 6

        for next_hole in hole.adj:
            if not next_hole.colored:
                self.color_hole_iter(board, next_hole)

    def print_melting_cheese(self, board=None):
        if board is None:
            board = self.board

        print()
        print("--" * len(board[0]))
        for row in board:
            for e in row:
                if e == 0:
                    print(colorful.black(e), end=' ')
                elif e == 1:
                    print(colorful.yellow(e), end=' ')
                elif e == 6:
                    print(colorful.red('c'), end=' ')
                elif e == 7:
                    print(colorful.blue('h'), end=' ')
            print()
        print("--" * len(board[0]))

    def is_opened_hole(self, hole):
        if hole.mode == 'row':
            get_edge = self.get_row_edge
        elif hole.mode == 'col':
            get_edge = self.get_col_edge

        upper_edge = get_edge(hole.idx - 1)
        lower_edge = get_edge(hole.idx + 1)

        if upper_edge is None or upper_edge[0] > hole.left + 1 or upper_edge[1] < hole.right - 1:
            return True
        elif lower_edge is None or lower_edge[0] > hole.left + 1 or lower_edge[1] < hole.right - 1:
            return True
        else: 
            return False

    def update_hole_status(self, mode):
        if mode == 'row':
            is_empty = self.is_row_empty
            hole_list = self.row_hole
        elif mode == 'col':
            is_empty = self.is_col_empty
            hole_list = self.col_hole

        for i in range(len(is_empty)):
            if is_empty[i]:
                continue

            for hole in hole_list.get(i, []):
                if self.is_opened_hole(hole):
                    self.opened_holes.append(hole)

                next_holes = hole_list.get(i+1, [])
                for another in next_holes:
                    if hole.is_connected(another):
                        hole.add_neighbor(another)

    def solve(self, plot=False):
        hour = 0
        count = 0
        while sum(self.is_row_empty) != len(self.is_row_empty):
            self.solve_iter()
            hour += 1
            if plot:
                self.print_melting_cheese()
            count = self.count_melting()

        print(hour)
        print(count)

    def solve_iter(self):
        self.edge_iter('row')
        self.edge_iter('col')

        self.hole_iter('row')
        self.hole_iter('col')

        self.update_hole_status('row')
        self.update_hole_status('col')

        self.color_row_edge(self.board)
        self.color_col_edge(self.board)
        self.color_opened_hole(self.board)

        self.row_hole = dict()
        self.col_hole = dict()
        self.opened_holes = list()

    def count_melting(self):
        count = 0 
        for i, row in enumerate(self.board):
            for j, e in enumerate(row):
                if e == 6:
                    count += 1
                    self.board[i][j] = 0

            if all(e == 0 for e in row):
                self.is_row_empty[i] = True

        return count


class Hole:
    def __init__(self, hole, mode, idx):
        self.left = hole[0]
        self.right = hole[1]
        
        self.mode = mode # row or col
        self.idx  = idx

        self.adj = list()
        self.colored = False

    def __repr__(self):
        #return f"({self.left},{self.right})"
        neighbor_list = ",".join([f"({neighbor.left}, {neighbor.right})" for neighbor in self.adj])
        return f"Hole(({self.left},{self.right}), {self.mode}, {self.idx}) - [{neighbor_list}]"

    def __eq__(self, another):
        return self.left == another.left and self.right == another.right and self.mode == another.mode and self.idx == another.idx

    def add_neighbor(self, another):
        self.adj.append(another)
        another.adj.append(self)

    def is_connected(self, another):
        set1 = set(range(self.left + 1, self.right))
        set2 = set(range(another.left + 1, another.right))
        return len(set1 & set2) > 0


def main():
    ROW, COL = [int(i) for i in input().split()]
    board = list()
    for _ in range(ROW):
        board.append(input())
    board = "\n".join(board)
    cheese = Cheese(board)
    cheese.solve()

if __name__ == '__main__':
    main()
