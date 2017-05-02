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
            
    def row_edge_iter(self):
        for i, row in enumerate(self.board):
            if self.is_row_empty[i]:
                continue
                            
            row = self.row(i)
            self.row_first[i] = self.first_cheese(row, self.row_first.get(i, 0))
            self.row_last[i]  = self.last_cheese(row, self.row_last.get(i, len(row)-1))
            
            if self.row_first[i] == len(row)-1:
                self.is_row_empty[i] = True

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
                found.append((hole_left, hole_right))
                hole_right = self.first_cheese(line, hole_right)

            if len(found) > 0:
                hole_list[i] = found

    def row_hole_iter(self):
        for i, row in enumerate(self.board):
            if self.is_row_empty[i]:
                continue
                            
            row = self.row(i)
            hole_right = self.first_cheese(row, self.row_first[i])
            holes_list = list()
            while hole_right <= self.row_last[i]:
                hole_left = self.last_cheese(row, hole_right)
                holes_list.append((hole_left, hole_right))
                hole_right = self.first_cheese(row, hole_right)

            if len(holes_list) > 0:
                self.row_hole[i] = holes_list
            
    def get_row_hole(self, i):
        return self.row_hole.get(i, None)

    def get_col_hole(self, i):
        return self.col_hole.get(i, None)
                    
    def has_hole(self, i):
        return len(self.row_hole[i]) > 0
            
    def explore_row_hole(self, idx, direction):
        cur_left, cur_right = self.row_hole[idx].pop(0)
        
        next_left, next_right = next_holes[0]
        if next_left <= cur_right:
            self.explore_row_hole(self, idx + direction, direction)

    def color_row_edge(self, board):
        for i in range(len(board)):
            if self.is_row_empty[i]:
                continue

            edge = self.get_row_edge(i)
            if edge is not None:
                board[i][edge[0]] = 6
                board[i][edge[1]] = 6
        return board

    def color_row_hole(self, board):
        for i in range(len(board)):
            if self.is_row_empty[i]:
                continue

            hole = self.get_row_hole(i)
            if hole is None:
                continue

            for h in hole:
                board[i][h[0]] = 7
                board[i][h[1]] = 7
        return board

    def color_col_edge(self, board):
        for i in range(len(board[0])):
            if self.is_col_empty[i]:
                continue

            edge = self.get_col_edge(i)
            if edge is not None:
                board[edge[0]][i] = 6
                board[edge[1]][i] = 6
        return board

    def color_col_hole(self, board):
        for i in range(len(board[0])):
            if self.is_col_empty[i]:
                continue

            hole = self.get_col_hole(i)
            if hole is None:
                continue

            for h in hole:
                board[h[0]][i] = 7
                board[h[1]][i] = 7
        return board

    def print_melting_cheese(self, board):
        for row in board:
            print()
            for e in row:
                if e == 0:
                    print(colorful.black(e), end=' ')
                elif e == 1:
                    print(colorful.yellow(e), end=' ')
                elif e == 6:
                    print(colorful.red('c'), end=' ')
                elif e == 7:
                    print(colorful.blue('h'), end=' ')

    def is_opened_row_hole(self, row_hole):
        upper_edge = get_row_edge(row_hole.idx - 1)
        lower_edge = get_row_edge(row_hole.idx + 1)

        if upper_edge is None or upper_edge[0] > row_hole.left + 1 or upper_edge[1] < row_hole.right - 1:
            return True

        if lower_edge is None or lower_edge[0] > row_hole.left + 1 or lower_edge[1] < row_hole.right - 1:
            return True

class Hole:
    def __init__(self, hole, mode, idx):
        self.left = hole[0]
        self.right = hole[1]
        
        self.mode = mode # row or col
        self.idx  = idx

        self.adj = list()

    def add_neighbor(self, another):
        self.adj.append(another)
        another.adj.append(self)
