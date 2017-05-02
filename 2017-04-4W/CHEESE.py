class Cheese:
    def __init__(self, board):
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

    def cheese_idx(self, line):
        return [i for i in range(len(line)) if line[i] == 1]
            
    def get_melting_cheese(self, line):
        cheese = self.cheese_idx(line)
        return [cheese[0], cheese[-1]]
            
    def edge_iter(self, line, begin, end):
        ret = list()
        for i in range(begin + 1, end):
            if line[i] == 0 and line[i+1] == 1:
                ret.append(i+1)
    
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

    def get_row_edge(self, i):
        if self.is_row_empty[i]:
            return None
        else:
            return self.row_first[i], self.row_last[i]

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
                    
    def has_hole(self, i):
        return len(self.row_hole[i]) > 0
            
    def explore_row_hole(self, idx, direction):
        cur_left, cur_right = self.row_hole[idx].pop(0)
        
        next_left, next_right = next_holes[0]
        if next_left <= cur_right:
            self.explore_row_hole(self, idx + direction, direction)


class Hole:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.adj = list()
